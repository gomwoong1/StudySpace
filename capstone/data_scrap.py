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


item = driver.find_element(By.CLASS_NAME, "qna")
# item.click()

time.sleep(5)

# driver.close()