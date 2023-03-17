# 연습문제2.pdf

# Q1. 홍길동씨 평균점수 구하기
score = [80, 75, 55]
print(sum(score)/len(score))

# Q2. 자연수 13이 홀수인지 짝수인지 판별할 수 있는 방법에 대해 말해보자
# 13을 나머지 연산자를 활용해 2로 나누었을 때, 나머지가 발생하면 홀수, 없다면 짝수입니다.
val = 13
result = "짝수" if val % 2 == 0 else "홀수"

# Q3. 홍길동씨의 주민번호를 나누어 출력해보기
pin = "881120-1068234"
yyyymmdd = pin[:6]
num = pin[-7:]
print(yyyymmdd)
print(num)

# Q4. 주민등록번호에서 성별을 나타내는 숫자 출력하기
pin = "881120-1068234"
print(pin[7])

# Q5. replace 함수를 사용해 문자열 바꿔서 출력하기
a = "a:b:c:d"
b = a.replace(":", "#")
print(b)

# Q6. 리스트의 원소 순서를 바꿔서 출력하기
a = [1, 3, 5, 4, 2]
a.sort()
a.reverse()
print(a)

# Q7. 리스트의 원소를 문자열로 만들어 출력하기
a = ["Life", "is", "too", "short"]
result = ' '.join(a)
print(result)

# Q8. 튜플에 값 추가하기
a = (1, 2, 3)
a += (4,)
print(a)

# Q9. 객관식 - 딕셔너리
# 3번. 리스트를 key값으로 사용할 수 없다.

# Q10. 딕셔너리 값 추출
a = {'A':90, 'B':80, 'C':70}
result = a.get('B')
print(result)

# Q11. 리스트 중복 제거
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
aSet = set(a)
b = list(aSet)
print(b)

# Q12. 동시 선언에 관한 문제
# 리스트 b의 값도 같이 변경된다.
# 파이썬의 모든 변수들은 참조변수이며, 동시 선언한 변수는
# 같은 주소값을 공유하기 때문이다.


# 연습문제3.pdf

# Q1. 코드의 결과값
# shirt

# Q2. while문 사용해 1~1000 중 3의 배수의 합을 구하기

result = 0
i = 1
while i <= 1000:
  if i % 3 == 0:
    result += i
  i += 1

print(result)

# Q3. 별찍기
i = 0
while True:
  i += 1
  if i > 5: break
  print("*"*i)

# Q4. 1~100 출력하기
for i in range(1, 101):
  print(i)

# Q5. for문 이용해 평균점수 구하기
A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0
for score in A:
  total += score
average = total/len(A)
print(average)

