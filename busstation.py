from sqlite3 import IntegrityError
import pandas as pd

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

import os
import django
from Cheonggye_dong.models import Bus

import pandas as pd
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

def get_stations(loc):
    #################### 해당 loc정보로 polygon모양(객체) 만들어주기 #########################3
    loc_result = []
    
    for i in range(0,len(loc),2):
        loc_result.append((float(loc[i]),float(loc[i+1])))

    polygon = Polygon(loc_result)
 
    ########### Model 비우기 ###################################
    old_datas = Bus.objects.all()
    old_datas.delete()

    ############################### 장고 모델로 데이터 저장하기 위한 셋팅 ##################################
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', "MyBus.settings")
    django.setup()

    ################################ csv파일에서 해당 다각형 범위에 있는 버스정류장 정보 가져오기 ########################
    df = pd.read_csv("전국버스정류장 위치정보.csv",encoding="ANSI")
    df = df[df["도시명"]=="화성시"] # 화성시 파일만 추출
    df = df[df.apply(lambda x: polygon.contains(Point(x['위도'], x['경도'])), axis=1)] # 위에서 만든 polygon객체에 포함되는 데이터만 추출
    print("걸러진 데이터 확인용___________________________________")
    print(df)
    # df = df.to_json(orient="records")

    ############################### 해당 버스정류장을 거치는 버스 정보 크롤링하기 ##############################
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    dr = webdriver.Chrome("C:\Git_repository\MyStudy\chromedriver.exe", options=options) #웹드라이버로 크롬 웹 켜기
    wait = WebDriverWait(dr, 7)
    dr.maximize_window()
    dr.get('https://www.gbis.go.kr/gbis2014/schBus.action?mapTabCd=1') 
    
    stations = df["단축아이디"] # 네모 칸 안에 있는 정류장 고유번호를 담은 리스트
    print(len(stations)) ############################################################################################  !!!! 네모 칸 안에 있는 정류장 갯수 !!!!!!!

    for station in stations:
        print("정류장번호",station,"---------------------------")
        while True:
            try:
                input = wait.until(EC.element_to_be_clickable((By.ID, "bisSearchKeyword")))
                print("1번")
                input.clear()
                input.send_keys(int(station))
                input.send_keys(Keys.ENTER)
                print("2번")
                # time.sleep(3)
                station_results = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".station.active")))
                station_results.click()
                print("3번")
                time.sleep(0.5)
                station_result = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a#list_station_0")))
                station_result.click()
                print("4번")
                time.sleep(0.5)
                wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.station_bus_list > ul > li > div > a")))
                print("5번")
                # time.sleep(3)
                bus_results_box = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.station_bus_list > ul")))
                print("6번")
                bus_results = bus_results_box.find_elements(By.TAG_NAME,"li")
                print("버스갯수",len(bus_results))
                for bus_result in bus_results:
                    bus = bus_result.find_elements(By.CSS_SELECTOR,"div.s_bus_num > a > strong")
                    print(bus[0].text)
                    try:
                        Bus(bus_num=bus[0].text).save()
                    except:
                        print("-------------중복의심데이터검출----------------------")
                        continue
                break
            
            except Exception as e:
                print(e)
                print("-------------------오류-------------------")
    print("--------------------------------성공--------------------------------------------")
    result = Bus.objects.all()
    return (len(stations),len(result))

