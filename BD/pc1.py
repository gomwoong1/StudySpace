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

