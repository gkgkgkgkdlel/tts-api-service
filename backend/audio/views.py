from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json
import re
from .models import Audio, Project, Text, TextList


# Create your views here.


class CreateAudioView(APIView):
    def post(self, request):

        datas = json.loads(request.body)
        project_title = datas["project_title"]

        Project.objects.create(project_title=project_title)
        project_id = Project.objects.latest("id").id

        text_list = datas["text"]
        id = 1
        preprocessed_text_list = []

        for text in text_list:
            pattern = "[^\w\s?.!ㄱ-ㅎ가-힣]"

            if re.search(pattern, text):
                text = re.sub(pattern, "", text)

            pattern = "[\w\sㄱ-ㅎ가-힣]+[.!?]"

            result = re.findall(pattern, text)  # .!? 기준으로 문장 나누기
            result = list(map(lambda x: x.strip(), result))  # 문장 앞뒤 공백 제거

            preprocessed_text_list.append(result)

        texts_dict = tts(
            project_id,
            preprocessed_text_list,
            "static/audio/" + str(project_id) + ".mp3",
        )
        return Response({"texts_dict": texts_dict})


class ReadTextView(APIView):
    def get(self, request):

        project_id = request.GET.get("project_id", None)
        page = request.GET.get("page", None)

        audio_id = Audio.objects.get(project_id=project_id).id

        text_id = Text.objects.filter(audio_id=audio_id).latest("id").id

        start_index = (int(page) - 1) * 10
        end_index = start_index + 9
        sentences_set = TextList.objects.filter(
            sentence_idx__gte=start_index,
            sentence_idx__lte=end_index,
            text_id=text_id,
        ).order_by("sentence_idx")
        i = 1
        sentence_result = {
            i: sentences_set[i].sentence for i in range(0, len(sentences_set))
        }

        return Response(sentence_result)


def tts(project_id, text_list, path):

    project_obj = Project.objects.get(id=project_id)
    Audio.objects.create(project_id=project_obj, audio_file=path)
    audio_id = Audio.objects.latest("id")
    i = 0
    texts_dict = {}

    for text in text_list:
        Text.objects.create(text=text, idx=i, audio_id=audio_id)
        texts_dict[i] = text
        i = i + 1

        text_id = Text.objects.latest("id").id
        text_obj = Text.objects.get(id=text_id)
        text_sentences = text_obj.text
        text_sentences = text_sentences[1 : len(text_sentences) - 1]
        text_sentences = text_sentences.split(",")

        idx = 0

        for text_sentence in text_sentences:
            TextList.objects.create(
                sentence_idx=idx, text_id=text_obj, sentence=text_sentence
            )
            idx = idx + 1

    return texts_dict


class UpdateTextView(APIView):
    def put(self, request):
        data = json.loads(request.body)
        project_id = data["project_id"]
        sentence_idx = data["sentence_idx"]
        sentence = data["sentence"]
        speed = data["speed"]

        audio_obj = Audio.objects.get(project_id=project_id)
        audio_obj.speed = speed
        audio_obj.save()

        audio_id = audio_obj.id
        text_id = Text.objects.filter(audio_id=audio_id).latest("id").id
        textlist_obj = TextList.objects.get(
            text_id=text_id, sentence_idx=sentence_idx
        )
        textlist_obj.sentence = sentence
        textlist_obj.save()

        return Response(status=status.HTTP_201_CREATED)


class GetAudioFileView(APIView):
    def get(self, request):
        project_id = request.GET.get("project_id", None)
        audio_obj = Audio.objects.get(project_id=project_id)
        audio_file = audio_obj.audio_file

        return Response({"audio_file": str(audio_file)})


class InsertTextView(APIView):
    def post(self, request):
        data = json.loads(request.body)
        project_id = data["project_id"]
        text = data["text"]
        text_idx = data["text_idx"]

        audio_obj = Audio.objects.get(project_id=project_id)
        text_objs = Text.objects.filter(
            audio_id=audio_obj.id, idx__gt=text_idx
        )

        for text_obj in text_objs:
            text_obj.idx = text_obj.idx + 1
            text_obj.save()

        preprocessed_text_list = []

        pattern = "[^\w\s?.!ㄱ-ㅎ가-힣]"

        if re.search(pattern, text):
            text = re.sub(pattern, "", text)

        pattern = "[\w\sㄱ-ㅎ가-힣]+[.!?]"

        result = re.findall(pattern, text)  # .!? 기준으로 문장 나누기
        result = list(map(lambda x: x.strip(), result))  # 문장 앞뒤 공백 제거

        preprocessed_text_list.append(result)

        Text.objects.create(
            idx=text_idx, text=preprocessed_text_list, audio_id=audio_obj
        )

        """
        Text 정보들로 새로운 오디오 파일을 생성했다고 가정.
        """
        new_audio_file = "static/audio/updated_" + str(project_id) + ".mp3"
        audio_obj.audio_file = new_audio_file

        audio_obj.save()

        return Response(status=status.HTTP_201_CREATED)


class DeleteProjectView(APIView):
    def get(self, request, project_id):
        print("project_id는 ", project_id)
        project_obj = Project.objects.get(id=project_id)
        project_obj.delete()

        return Response(status=status.HTTP_200_OK)
