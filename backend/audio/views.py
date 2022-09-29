from rest_framework.views import APIView
from rest_framework.response import Response
import json

# Create your views here.


class TextView(APIView):
    def get(self, request):
        return Response({"테스트 중입니다"})


class CreateAudioView(APIView):
    def post(self, request):
        datas = json.loads(request.body)
        text_list = datas["text"]
        i = 1
        for text in text_list:
            print(i, ": ", text)
            i = i + 1

        return Response({"text_list": text_list})
