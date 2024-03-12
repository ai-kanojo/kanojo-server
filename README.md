# kanojo-server
ai-kanojo의 서버를 담당하는 레포지토리입니다.

## 기본 환경 설정

```bash
# 가상 환경 생성
$ python3 -m venv venv
```

```bash
# 가상 환경 활성화
$ source venv/bin/activate
```

```bash
# 가상 환경 비활성화
$ deactivate
```

```bash
# requirement.txt에 적힌 패키지 설치
$ pip3 install -r requirements.txt
```

```bash
# 패키지 의존성 저장
# pip를 통해 패키지를 설치한 후에는 반드시 requirement에 기록합니다.
$ pip3 freeze > requirement.txt
```

## flask 실행

```bash
# api 서버 실행
$ python3 main.py
```

- http://localhost:5000 에서 api 서버가 실행됩니다.
