from rest_framework.views import APIView
from rest_framework.response import Response
import json
import re
from .models import Audio, Project, Text, TextList


# Create your views here.


class TextView(APIView):
    def get(self, request):
        return Response({"테스트 중입니다"})


class CreateAudioView(APIView):
    def post(self, request):

        datas = json.loads(request.body)
        project_title = datas["project_title"]

        Project.objects.create(project_title=project_title)
        project_id = Project.objects.latest("id").id
        print("project_id는 ", project_id)

        text_list = datas["text"]
        id = 1
        preprocessed_text_list = []

        for text in text_list:
            pattern = "[^\w\s?.!ㄱ-ㅎ가-힣]"
            print(re.search(pattern, text))
            if re.search(pattern, text):
                text = re.sub(pattern, "", text)

            pattern = "[\w\sㄱ-ㅎ가-힣]+[.!?]"
            # result = re.search(pattern, text)
            result = re.findall(pattern, text)
            result = list(map(lambda x: x.strip(), result))  # 문장 앞뒤 공백 제거

            # texts_dict = {(i + 1): result[i] for i in range(0, len(result))}    # 하나의 텍스트를 여러 개의 문장으로 idx값 붙여줌.
            # texts_dict[id] = result

            preprocessed_text_list.append(result)

        texts_dict = tts(
            project_id,
            preprocessed_text_list,
            "static/audio/" + str(project_id) + ".mp3",
        )
        return Response({"texts_dict": texts_dict})


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

        print("@@text_sentence는 ", text_sentences)
        idx = 0
        print("text는 ", text)
        for text_sentence in text_sentences:
            print("text_sentence는 ", text_sentence)
            TextList.objects.create(
                sentence_idx=idx, text_id=text_obj, sentence=text_sentence
            )
            idx = idx + 1

    return texts_dict
