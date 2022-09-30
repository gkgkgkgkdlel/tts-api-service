# tts-api-service
# 📎 목차

1. [tts-api-service]
2. [개발 기간]
3. [요구사항 및 분석]
4. [기술 스택]
5. [API Endpoints]


# 🚀 게시글 crud api 서비스

# 📆 개발 기간
- 2022.09.28 ~ 2022.09.30


# 📝 요구사항 및 분석
### 1. 프로젝트 생성(오디오 생성)

-  텍스트(str)가 담긴 리스트를 받습니다. (length = 1)
- 이를 전처리하여 오디오를 생성하는 함수의 input으로 같이 넣습니다.
[['text1', 'text2', 'text3', ....], path]
- 일정시간 이후 함수에서 (id, text)형태의 원소를 가진 리스트를 리턴합니다.
[('id1' ,'text1'), ('id2', 'text2'), ('id3', 'text3'), ....]
- 오디오는 input의 path에 저장됩니다.

### 2. 텍스트 조회

- 특정 프로젝트의 n번째 페이지를 조회합니다.
- 한페이지는 10문장으로 이루어져 있습니다.


### 3. 텍스트 수정

- 한 문장의 텍스트와 스피드를 수정합니다.

### 4. 오디오파일 송신

- 요청받은 오디오파일을 송신합니다

### 5. 텍스트(오디오) 생성 / 삭제

- 삽입위치는 항상 앞, 뒤가 아닌 중간도 가능


### 5. 프로젝트 삭제


# 🛠 기술 스택
Language | Framwork | Database | HTTP | Develop | Tools
| :----------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------: |
| <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"> | <img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white"> | <img src="https://img.shields.io/badge/mysql-4479A1?style=for-the-badge&logo=mysql&logoColor=white"> | <img src="https://img.shields.io/badge/postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white"> | <img src="https://img.shields.io/badge/discord-5865F2?style=for-the-badge&logo=discord&logoColor=white"> <img src="https://img.shields.io/badge/git-F05032?style=for-the-badge&logo=git&logoColor=white"> 

# 🎯 API Endpoints
| endpoint | HTTP Method | 기능   | require parameter                                                                                                   | response data |
|----------|-------------|------|---------------------------------------------------------------------------------------------------------------------|---------------|
| /create/ | POST | 프로젝트 생성 | project_title: string | text_dict: json |
| /read/ | GET | 텍스트 조회 | project_id: string, page: string | sentence_result: json |
| /update/| PUT | 텍스트 수정 | project_id: int, sentence_idx: int, sentence: string, speed: int | 성공 여부 |
| /audio_file/| GET | 오디오파일 송신| project_id: int| audio_file:string |
| /insert_audio_file/| POST | 텍스트 생성/삭제 | project_id: int, text: string, text_idx: int | 성공 여부 |
| /delete/<int:project_id>/ | DELETE | 프로젝트 삭제 | project_id:| 성공 여부 |
