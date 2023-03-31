# 서울시 대중교통 GTFS 프로젝트

서울시 대중교통중 GTFS화된 데이터가 없어서(적어도 공개된 데이터는 없더라) 직접 만드는 프로젝트.

## 체크리스트
- [x] agency (운송업체)
- [x] stops (정류소)
- [ ] routes (노선; 세부경로로 이루어짐)
- [ ] trips (세부경로; 특정 기간에 정류장 2곳 이상을 이동)
- [ ] stop_times (차량이 각 경로마다 정류장에 도착하고 출발하는 시간)
- [ ] calendar (서비스 날짜 - 시작과 종료일)
- [ ] calendar_dates (서비스 예외날짜)
- [ ] fare_attributes (대중교통 요금)
- [ ] fare_rules (요금 규칙)
- [ ] shapes (쉐이프)
- [ ] frequencies (운행 간격)
- [ ] pathways (역 내 이동 통로)
- [ ] transfers (환승 지점 연결 방식)
- [ ] levels (역 내 층수)
- [ ] feed_info (메타데이터)
- [ ] translations (번역 정보)
- [ ] attributions (데이터셋 속성)

## 사용법
### 공통
1. 가상환경을 만든다.
2. requirements 파일로 필요 라이브러리를 다운 받는다.
```bash
python -m venv gtfs_env
pip install -r requirements.txt
```
3. 나중에 만들 main.py 파일을 실행한다

### 작업 잡소리
* route를 만들어보니까 지금까지 작성한 애들은 다시 리팩터링 해야할 듯. 데이터 작성에서 끝내지 말고 어차피 나중에 다시 참조해서 id 받아와야 되니까 작성된 데이터를 함수별로 리턴하자.
* 모든 작업에 필요한 최소 데이터는 busRouteId다. 이 파일은 [서울 열린데이터 광장](data.seoul.go.kr)에서 "서울시 버스노선 기본정보 항목정보"로 찾을 수 있다.

### Todo
* [x] 지금 경로가 다 내 기준으로 작성됐는데 전부다 absolute 경로로 바꾸기
* [ ] 하나만 돌려도 되게끔 main.py 파일 만들기