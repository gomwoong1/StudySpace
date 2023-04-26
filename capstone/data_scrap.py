# 정적 웹 크롤링으론 불가능
# import requests
# from bs4 import BeautifulSoup

from selenium import webdriver 
from selenium.webdriver.common.by import By

import time

# 시스템에 부착된 장치가 작동하지 않습니다. (0x1F) 에러 제어용 코드
# driver = webdriver.Chrome() 코드에 대한 에러 제어
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)

# 페이지 로딩을 위한 5초 대기
driver.implicitly_wait(5)

# URL에 접근
driver.get('https://www.univ100.kr/qna/344')

# 페이지 로딩을 위한 5초 대기
driver.implicitly_wait(5)

items = driver.find_elements(By.CLASS_NAME, "qna")

scroll_location = driver.execute_script("return document.body.scrollHeight")

while True:
	#현재 스크롤의 가장 아래로 내림
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    
    #전체 스크롤이 늘어날 때까지 대기
    time.sleep(2)
    
    #늘어난 스크롤 높이
    scroll_height = driver.execute_script("return document.body.scrollHeight")

    #늘어난 스크롤 위치와 이동 전 위치 같으면(더 이상 스크롤이 늘어나지 않으면) 종료
    if scroll_location == scroll_height:
        break
	
    #같지 않으면 스크롤 위치 값을 수정하여 같아질 때까지 반복
    else:
        #스크롤 위치값을 수정
        scroll_location = driver.execute_script("return document.body.scrollHeight")



# items = driver.find_elements(By.CLASS_NAME, "qna")
# # for i in items:
# #     print(i.click())

# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# items.append(driver.find_elements(By.CLASS_NAME, "qna"))


# print(len(items))

time.sleep(3)

driver.close()