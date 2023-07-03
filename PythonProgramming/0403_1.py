# --------------------------- #
# 기본형 데이터 타입 예제 소스 #
# --------------------------- #

a = "Python Programming"
print("a의 0 ~ 1번 문자:", a[:2])
print("a의 3번 ~ 끝까지의 문자:", a[3:])
print("a의 0 ~ 4번 문자:", a[:5])
print("a의 처음 ~ 끝까지의 문자:", a[:])

a = "20330518Monday"
year = a[:4]
print("a의 0 ~ 3번 문자", year)

month = a[4:6]
print("a의 4 ~ 5번 문자",month)

day = a[6:8]
print("a의 6 ~ 7번 문자",day)

week = a[8:]
print("a의 8번 ~ 끝까지의 문자", week)
print("슬라이싱 합쳐서 출력:", year + "년 " + month + "월 " + day + "일 " + week)

a = "Sprce"
print(a[:2])
print(a[3:])
print("Scpre 오타 수정:", a[:2] + 'a' + a[3:])

a = "Spacezone"
print("a의 개수:", a.count('a'))

a = "I can do it"
print("a의 인덱스 번호:",a.find('a'))
print("do의 인덱스 번호:",a.find('do'))
print("s의 인덱스 번호:",a.find('s'))

a = "Have a good time"
print("a의 인덱스 번호:",a.index('a'))
print("me의 인덱스 번호:",a.index('me'))
# print(a.index('c'))

a = " power "
print("양쪽 공백 제거:", a.strip())
print("왼쪽 공백 제거:", a.lstrip())
print("오른쪽 공백 제거:",a.rstrip())

a = "Speed Zone"
print("대문자: ", a.upper())
print("소문자: ", a.lower())

a = " / "
print("/ 삽입하기", a.join('asdf'))

a = " or "
print("or 삽입하기", a.join('asdf'))

a = "speed zone"
print("문자열 대체:", a.replace("speed", "power"))

a = "One Two Three"
print("공백 기준 문자열 쪼개기", a.split())

a = "spring:summer:fall:winter"
print("':' 기준 문자열 쪼개기", a.split(':'))

a = (100 < 100)
print("100이 100보다 크다:", a)

b = (300 == 300)
print("300은 300과 같다:", b)

c = True
print("True의 자료형은:",type(c))