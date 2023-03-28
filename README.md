# 서울시 대중교통 GTFS 프로젝트

서울시 대중교통중 GTFS화된 데이터가 없어서(적어도 공개된 데이터는 없더라) 직접 만드는 프로젝트.

## 체크리스트
- agency [완료]
- stops
- routes
- trips
- stop_times
- calendar
- calendar_dates
- fare_attributes
- fare_rules
- shapes
- pathways
- frequencies
- transfers
- levels
- translations
- attributions

## 사용법
### 공통
1. 가상환경을 만든다.
2. requirements 파일로 필요 라이브러리를 다운 받는다.
```bash
python -m venv gtfs_env
pip install -r requirements.txt
```
3. 나중에 만들 main.py 파일을 실행한다

### Agency
1. [서울시 TOPIS](https://topis.seoul.go.kr/refRoom/openRefRoom_3_1.do)에서 월별 운행노선 현황을 다운 받는다.
2. 엑셀 파일을 열고 첫 줄을 지운다.
3. builds.py 에서 `build_agency()`함수를 돌린다. 

### Todo
* 지금 경로가 다 내 기준으로 작성됐는데 전부다 absolute 경로로 바꾸기
* 하나만 돌려도 되게끔 main.py 파일 만들기