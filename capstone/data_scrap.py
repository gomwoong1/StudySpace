# 정적 웹 크롤링으론 불가능
# import requests
# from bs4 import BeautifulSoup

from selenium import webdriver 

driver = webdriver.Chrome()
driver.get('https://www.univ100.kr/qna/344')

