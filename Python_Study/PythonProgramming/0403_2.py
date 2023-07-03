## 김지웅_컴퓨터시스템과_3학년_201945018_파이선 4장과제물 ##
print("-"*50)
print("김지웅 201945018 4장 과제물")
print("="*50)

a = 9
b = 2
print("a//b의 결과값:", a//b, "-a//b의 결과값:", -a//b)

print("My name's Kim Ji Woong")
c = "My name is Kim Ji Woong"
print("문자열 c중, 's'의 개수", c.count('s'))

d = "Bythom Programing"
print("'Bythom Programing'의 오타 수정: P" + d[1:5] + "n" + d[6:14] + "m" + d[14:])

e = "inha"
print("소문자 'inha' 대문자로 변환:", e.upper())

f = "I like INHA"
print("'like'를 'love'로 대체", f.replace("like", "love"))

g = "20250401Monday"
year = g[:4]
month = g[4:6]
day = g[6:8]
week = g[8:]
print("슬라이싱을 이용한 문자열 합치기 결과:", year + "년 " + month + "월 " + day + "일 " + week)