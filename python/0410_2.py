# 컴퓨터시스템과 A반 김지웅 5장 과제물

print("-"*52)
print("컴퓨터시스템과 A반 학번:201945018 김지웅 5장 과제물")
print("="*52)

a = [101, 102, ['One', 'Two', 'Three'], 103, 104, 105]
print("리스트 a의 2~4번째 요소:", a[1:4])

a = [88, 35, 97, 35, 88]
a.remove(35)
print("리스트 a에서 35를 제거한 결과:", a)

tp = (101, 102, 'one', 'two')
print('튜플 tp에서 2번째부터 마지막까지의 요소 출력:', tp[2:])

a = {101:'smart'}
a[201] = 'graphic'
print("딕셔너리 a에서 키 201, 값 'graphic'을 추가한 후 출력:", a)

b = {101:'coding', 'id':'python'}
del b['id']
print("딕셔너리 b에서 키 'id'를 가진 쌍을 삭제한 후 출력", b)

c = {'id':'cskisa', 'pw':123456, 'email':'pkh@naver.com'}
print("딕셔너리 c의 키와 값을 쌍으로 출력:", c.items())

s3 = set('speed')
print("s3의 결과값 출력:", s3)

sd = set([101, 102, 103])
sd.add(105)
print("집합 sd에서 105를 추가한 결과:", sd)