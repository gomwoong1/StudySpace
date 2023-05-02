from selenium import webdriver 
from selenium.webdriver.common.by import By
import pandas as pd
import time

# pandas에 데이터를 삽입하는 함수
def insertData(number, title, category, dept, question, answer, comment):
    dataSet = [number, title, category, dept, question, answer, comment]
    data.loc[len(data)] = dataSet

data = pd.DataFrame(columns=['number', 'title', 'category', 'dept', 'question', 'answer','comment'])

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

# 페이지 로딩을 위한 3초 대기
time.sleep(3)

after_location = 0

# data_index 저장용 변수와 에러제어용 변수 선언
# i = 0
i = 606
cnt = 0 

try:
    while i < 1500:
    # while i < 2988:
        try:
            item = driver.find_element(By.CSS_SELECTOR, 'div[data-index="{}"]'.format(str(i))).click()
            
        except:
            print("{}를 찾는중!".format(i))
            
            cnt += 1
            
            driver.execute_script("window.scrollTo(0,{})".format(after_location + 100))
            
            #전체 스크롤이 늘어날 때까지 대기
            time.sleep(0.8)

            #이동 후 스크롤 위치
            after_location = driver.execute_script("return window.pageYOffset")
            print("이동 후 스크롤 위치:", after_location)

            continue
        
        time.sleep(2)
        # 질문 제목, 질문 내용, 학과, 카테고리, 질문 일시, 답변 text 긁어오기
        title = driver.find_element(By.CSS_SELECTOR, "h2[class='question__title']").text
        question = driver.find_element(By.CSS_SELECTOR, "div[class='question__text']").text
        dept = driver.find_element(By.CSS_SELECTOR, "div[class='question__profile']").text
        category = driver.find_element(By.CSS_SELECTOR, "span[class='question__category']").text
        date = driver.find_element(By.CSS_SELECTOR, "span[class='question__date']").text
        answers = driver.find_elements(By.CSS_SELECTOR, "article[class='answer']")

        if len(answers) == 0:
            insertData(i, title, category, dept, question, "None", "None")
        
        else:
            # 답변 개수 별 답변 매핑
            for answer in answers:
                
                # 답변의 댓글 찾아오기
                comments = answer.find_elements(By.CSS_SELECTOR, "article[class='comment']")

                # 답변 내용 긁어오기
                ans = answer.find_element(By.CSS_SELECTOR, "div[class='answer__text']").text

                comment_list = []
                # 답변의 댓글이 있는 경우, 댓글까지 한 번에 데이터 삽입
                if len(comments) != 0:
                    for comment in comments:
                        author = "[" + comment.find_element(By.CSS_SELECTOR, "div[class='comment__profile-text']").text + "]"
                        cmd = comment.find_element(By.CSS_SELECTOR, "div[class='comment__text']").text
                        comment_list.append(author+cmd)
                    commentResult = ';'.join(comment_list)
                    insertData(i, title, category, dept, question, ans, commentResult)
                
                # 답변의 댓글이 없는 경우, 댓글없이 한 번에 데이터 삽입
                else:
                    insertData(i, title, category, dept, question, ans, "None")

        # 뒤로가기 이후 스크롤이 위치를 잡지 못헀을 경우를 대비해 수동 이동
        driver.back()
        time.sleep(0.8)

        if driver.execute_script("return window.pageYOffset") == 0:
            driver.execute_script("window.scrollTo(0,{})".format(after_location))
            print("위치 복원:", after_location)
        i += 1
except:
    print("{}번쨰에서 에러발생, 중단".format(i))

finally:
    # dataFrame을 csv 파일로 변환
    data.to_csv('QnA.csv', encoding='utf-8-sig', index=False)
    driver.close()