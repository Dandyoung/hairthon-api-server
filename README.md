<br/>
<br/>

<p align="center">
<img src="https://files.cloudtype.io/logo/cloudtype-logo-horizontal-black.png" width="50%" alt="Cloudtype"/>
</p>

<br/>
<br/>

### 지원 Python 버전
- 3.7, 3.8, 3.9, 3.10, 3.11
- Flask는 최소 3.7 버전의 Python를 필요로 합니다.
- ⚠️ 로컬/테스트 환경과 클라우드타입에서 설정한 Python 버전이 상이한 경우 정상적으로 빌드되지 않을 수 있습니다.

## ⌨️ 명령어

### Start (1)

```bash
gunicorn -b 0.0.0.0:5000 app:app

```
이렇게해도 되고,

### Start (2)

```bash
flask run

```
이렇게 그대로 박아도된다~


### 로컬서버주소

```bash
http://127.0.0.1:5000/

```

