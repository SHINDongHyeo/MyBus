# 🚌MyBus
<b>주제 :</b> 우리 동네의 버스 정보를 분석하고 비교해 대중교통 사용이 편리하지 확인해본다               
<b>사용한 도구 :</b> <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white"/> <img src="https://img.shields.io/badge/Django-092E20?style=flat-square&logo=django&logoColor=white"/> <img src="https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white"/> <img src="https://img.shields.io/badge/Javascript-F7DF1E?style=flat-square&logo=javascript&logoColor=black"/> <img src="https://img.shields.io/badge/Kakao-FFCD00?style=flat-square&logo=kakao&logoColor=black"/>(map api), `공공데이터포털`[(https://www.data.go.kr/)](https://www.data.go.kr/)      
<b>핵심폴더 :</b> 루트 디렉토리에서 `Cheonggye_dong` 라는 application(폴더)을 만들고 해당 폴더에 코드를 작성했습니다.         

# 1.공공데이터
[https://www.data.go.kr/data/15067528/fileData.do](https://www.data.go.kr/data/15067528/fileData.do)에서 전국 버스정류장 정보 데이터를 받아왔다.         
1)`전국버스정류장 위치정보.csv` 예시

|    | 정류장아이디   | 정류장 명칭   |   정류장 유형 | 중앙차로 여부   | 노드영문명      |    위도 |    경도 | 수집일시            |   단축아이디 |   도시코드 | 도시명   |
|---:|:---------------|:--------------|--------------:|:----------------|:----------------|--------:|--------:|:--------------------|-------------:|-----------:|:---------|
|  1 | TSB254000097   | 구문소        |             1 | N               | Gumunso         | 37.0925 | 129.043 | 2021/09/16 04:01:26 |   2.5401e+06 |      32050 | 태백시   |
|  2 | TSB254000098   | 구문소        |             1 | N               | Gumunso         | 37.0924 | 129.043 | 2021/09/16 04:01:26 |   2.5401e+06 |      32050 | 태백시   |
|  3 | TSB254000099   | 사시랭이마을  |             1 | N               | Sasiraengimaeul | 37.0896 | 129.044 | 2021/09/16 04:01:26 |   

# 2.크롤링
경기버스정보[https://www.gbis.go.kr/](https://www.gbis.go.kr/)사이트를 통해 버스정류장 정보와 버스정보를 크롤링했다.

# 3.결과
<img src="https://github.com/SHINDongHyeo/MyBus/blob/main/images/%EA%B2%B0%EA%B3%BC1.png"/>            
<img src="https://github.com/SHINDongHyeo/MyBus/blob/main/images/%EA%B2%B0%EA%B3%BC2.png"/>