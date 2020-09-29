# 캡스톤 프로젝트

### 소개
() 웹서비스 소프트웨어입니다. <br/>
팀: 김재훈(팀장), 백동우, 윤채원, 이호진

### 서버 실행 명령어
```
# 깃 허브에서 소스코드를 다운로드 받습니다.
git clone git@github.com:kimja7045/side-mate-server.git

# 받은 프로젝트 폴더 경로로 이동합니다.
side-mate-server

# 프로젝트 내의 가상환경을 만들어줍니다.
python -m venv venv

# 가상환경을 활성화해줍니다.
. venv/bin/activate         - mac
. venv\Scripts\activate     - window

# 프로젝트에 사용된 모든 패키지를 간편하게 설치하기 위해 다음 명령어를 입력합니다. 
pip install -r requirements.txt

# 데이터베이스에 변경이 있으므로 이를 반영해주는 migrate 명령어를 입력합니다.
python manage.py migrate

# 웹 서버를 실행합니다.
python manage.py runserver
```
