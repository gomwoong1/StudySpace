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

# 창 최대화
driver.maximize_window()

# URL에 접근
driver.get('https://www.univ100.kr/qna/344')

# 페이지 로딩을 위한 1.5초 대기
time.sleep(1.5)

# 초기 스크롤 위치 설정
before_location = driver.execute_script("return window.pageYOffset")

# data_index 저장용 변수와 에러제어용 변수 선언
i = 0
cnt = 0 

while True:
    try:
        item = driver.find_element(By.CSS_SELECTOR, 'div[data-index="{}"]'.format(str(i))).click()
        
    except:
        print("{}를 찾는중!".format(i))
        
        cnt += 1
        
        if cnt > 3:
            # 스크롤이 너무 많이 넘어가서 못 찾는 경우를 대비
            driver.execute_script("window.scrollTo(0,{})".format(after_location - 1000))
            cnt = 0
            
        else :
            #현재 위치 + 200으로 스크롤 이동
            driver.execute_script("window.scrollTo(0,{})".format(before_location + 300))
        
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
            
        continue
    
    if(i > 1): break
    
    time.sleep(0.5)
    
    # 데이터 긁어오고 저장하는 영역
    
    # 질문 제목
    title = driver.find_element(By.CSS_SELECTOR, "h2[class='question__title']").text
    
    # 질문 내용
    content = driver.find_element(By.CSS_SELECTOR, "div[class='question__text']").text
    
    # 학과
    dept = driver.find_element(By.CSS_SELECTOR, "div[class='question__profile']").text
    
    # 카테고리
    category = driver.find_element(By.CSS_SELECTOR, "span[class='question__category']").text
    
    # 질문 일시
    date = driver.find_element(By.CSS_SELECTOR, "span[class='question__date']").text
    
    # 답변
    answers = driver.find_elements(By.CSS_SELECTOR, "div[class='answer__text']")

    print("\nnum: {}, title: {}\n".format(i, title))
    print("카테고리: {}, 학과: {}, 날짜: {}".format(category, dept, date))
    print(content)
    print("-"*100)

    for answer in answers:
        try:
            ans = answer.find_element(By.CSS_SELECTOR, "div[class='answer__text']").text
            print(ans)
            print("-"*100)
        except:
            print("\nnum: {}, title: {}\n".format(i, title))
            print("카테고리: {}, 학과: {}, 날짜: {}".format(category, dept, date))
            print(content)
            print("-"*100)
            print("")
    
    driver.back()
    time.sleep(0.5)
    i += 1

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