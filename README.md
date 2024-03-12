# kanojo-server

- ai-kanojo의 서버를 담당하는 레포지토리입니다.

## 최초 환경 설정

- 버전 관리를 위해 가상 환경을 사용합니다. 현재 디렉터리에 venv/ 가 없는 경우 가상 환경을 생성합니다.
- 가상 환경이 실행되면 의존성을 설치하여 프로그램을 실행합니다.

```bash
# 가상 환경 생성 ( 최초 환경 설정 시 )
$ python3 -m venv venv
```

```bash
# 가상 환경 활성화
$ source venv/bin/activate
```

```bash
# requirement.txt에 적힌 패키지 설치
$ pip3 install -r requirement.txt
```

```bash
# 패키지 의존성 저장
# pip를 통해 패키지를 설치한 후에는 반드시 requirement에 기록합니다.
$ pip3 freeze > requirement.txt
```

```bash
# 가상 환경 비활성화
$ deactivate
```

## flask 실행

```bash
# api 서버 실행
$ python3 main.py
```

- http://localhost:5000 에서 api 서버가 실행됩니다.
