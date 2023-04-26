import requests
from bs4 import BeautifulSoup


res = requests.get("https://www.univ100.kr/qna/344")
soup = BeautifulSoup(res.content, 'html.parser')

# val = soup.find("div", class_="school")
# print(val)
print(soup)