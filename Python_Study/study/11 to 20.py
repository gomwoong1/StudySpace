# 숫자(0~9)와 소수점(.)을 사용해 표현한 수를 실수(real number)라고 한다.

# 변수에 실수값을 저장한 후
# 변수에 저장되어 있는 값을 그대로 출력해보자.

# a = input()
# a = float(a)
# print(a)
#------------------------

# 줄을 바꿔 정수(integer) 2개를 입력받아 줄을 바꿔 출력해보자.

# a = int(input())
# b = int(input())
# print(a, b)
#------------------------

# 줄을 바꿔 문자(character) 2개를 입력받고, 순서를 바꿔 한 줄씩 출력해보자.

# a = input()
# b = input()
# print(b)
# print(a)
#------------------------

# 실수(real number) 1개를 입력받아 줄을 바꿔 3번 출력해보자.

# a = float(input())
# print(a)
# print(a)
# print(a)
#------------------------

# 공백을 두고 입력된정수(integer) 2개를 입력받아 줄을 바꿔 출력해보자.

# a, b = input().split()
# a = int(a)
# b = int(b)
# print(a, b)
#------------------------

# 공백을 두고 문자(character) 2개를 입력받아 순서를 바꿔 출력해보자.

# a, b = input().split()
# print(b,a)
#------------------------

# 정수(integer), 실수, 문자(character), 문자열(string) 등 1개만 입력받아 한 줄로 3번 출력해보자.

# a = input()
# print(a, a, a)

#------------------------

# 24시간 시:분 형식으로 시간이 입력될 때, 그대로 출력하는 연습을 해보자.

# hour, min = input().split(":")
# print(hour, min, sep=":")

#-------------------------

# "연도.월.일"을 입력받아 "일-월-연도" 순서로 바꿔 출력해보자.

# year, month, day = input().split(".")
# print(day, month, year, sep="-")

#--------------------------

# 주민번호는 다음과 같이 구성된다.
# XXXXXX-XXXXXXX

# 왼쪽 6자리는 생년월일(YYMMDD)이고, 오른쪽 7자리는 성별,출생지역,확인코드로 구성되어있다.
# 주민번호를 입력받아 형태를 바꿔 출력해보자.

# a, b = input().split("-")
# print(a+b)

#--------------------------
# input().split() 으로 여러 개 입력받고 구분가능함.
# split()의 매개변수에 "," 와 같이 문자로도 가능함.

# print(a, b, sep=".") 와 같이 sep 구분자 속성 사용하면 공백 대신 설정한 문자열 출력