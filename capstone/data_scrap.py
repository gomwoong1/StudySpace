from selenium import webdriver 
from selenium.webdriver.common.by import By
import time

# 시스템에 부착된 장치가 작동하지 않습니다. (0x1F) 에러 제어용 코드
# driver = webdriver.Chrome() 코드에 대한 에러 제어
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

# 페이지 리소스 모두 다운할 때까지 기다리는 옵션
options.page_load_strategy = 'normal'
driver = webdriver.Chrome(options=options)

# URL에 접근
driver.get('https://www.univ100.kr/qna/344')

# 페이지 로딩을 위한 1.5초 대기
time.sleep(1.5)

# 초기 스크롤 위치 설정
before_location = driver.execute_script("return window.pageYOffset")

# # # while True:
# for i in range(0, 1):
	

# while True:
    # i = 0
for i in range(0, 15, 1):
    try:
        item = driver.find_element(By.CSS_SELECTOR, 'div[data-index="{}"]'.format(str(i))).click()
        time.sleep(0.5)
        driver.back()
        time.sleep(0.5)
        #i += 1

    except:
        #현재 위치 + 500으로 스크롤 이동
        driver.execute_script("window.scrollTo(0,{})".format(before_location + 800))
            
        #전체 스크롤이 늘어날 때까지 대기
        time.sleep(0.3)

        #이동 후 스크롤 위치
        after_location = driver.execute_script("return window.pageYOffset")
        
        #이동후 위치와 이동 후 위치가 같으면(더 이상 스크롤이 늘어나지 않으면) 종료
        if before_location == after_location:
            break

        #같지 않으면 다음 조건 실행
        else:
            #이동여부 판단 기준이 되는 이전 위치 값 수정
            before_location = driver.execute_script("return window.pageYOffset")

# item = driver.find_element(By.CSS_SELECTOR, 'div[data-index="0"]')
# print("0:",item)
# item.click()
# time.sleep(3)
# driver.back()

# items = driver.find_elements(By.CLASS_NAME, "qna")
# item = driver.find_element(By.CSS_SELECTOR, '[data-index="9"]')
# print("9",item)
# item.click()


# 안 쓰지만 백업용
# while True:
# 	#현재 스크롤의 가장 아래로 내림
#     driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    
#     #전체 스크롤이 늘어날 때까지 대기
#     time.sleep(1)
#     # driver.implicitly_wait(1)
    
#     #늘어난 스크롤 높이
#     scroll_height = driver.execute_script("return document.body.scrollHeight")

#     #늘어난 스크롤 위치와 이동 전 위치 같으면(더 이상 스크롤이 늘어나지 않으면) 종료
#     if scroll_location == scroll_height:
#         break
	
#     #같지 않으면 스크롤 위치 값을 수정하여 같아질 때까지 반복
#     else:
#         #스크롤 위치값을 수정
#         scroll_location = driver.execute_script("return document.body.scrollHeight")

time.sleep(180)

driver.close()