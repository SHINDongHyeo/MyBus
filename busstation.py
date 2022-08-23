import pandas as pd

def get_stations():
    df = pd.read_csv("전국버스정류장 위치정보.csv",encoding="ANSI")
    df = df[df["도시명"]=="화성시"]
    lati_l = 37.193714 # 정류장 찾을 사각형 꼭짓점 정보
    lati_r = 37.205152 # 정류장 찾을 사각형 꼭짓점 정보
    long_u = 127.116086 # 정류장 찾을 사각형 꼭짓점 정보
    long_d = 127.095103 # 정류장 찾을 사각형 꼭짓점 정보
    df = df[(df["위도"]>=lati_l) & (df["위도"]<=lati_r) & (df["경도"]>=long_d) & (df["경도"]<=long_u)]
    df = df.to_json(orient="records")
    return df
