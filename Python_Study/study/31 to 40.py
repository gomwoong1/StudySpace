# 10진 정수 1개를 입력받아
# 유니코드 문자로 출력해보자.

# a = chr(int(input()))
# print(a)

#-----------------------------------

# 입력된 정수의 부호를 바꿔 출력해보자.

# a = int(input())
# print(-a)

#-----------------------------------

# 문자 1개를 입력받아 그 다음 문자를 출력해보자.
# 영문자 'A'의 다음 문자는 'B'이고, 숫자 '0'의 다음 문자는 '1'이다.

# a = chr(ord(input()) + 1)
# print(a)

#-----------------------------------

# 정수 2개(a, b)를 입력받아 a에서 b를 뺀 차를 출력하는 프로그램을 작성해보자.

# a, b = input().split()
# a, b  = int(a), int(b)
# print(a-b)

#-----------------------------------

# 실수 2개(f1, f2)를 입력받아 곱을 출력하는 프로그램을 작성해보자.

# a, b = input().split()
# a, b = float(a), float(b)
# print(a*b)

#-----------------------------------

# 단어와 반복 횟수를 입력받아 여러 번 출력해보자.

# a, b = input().split()
# print(a*int(b))

#-----------------------------------

# 반복 횟수와 문장을 입력받아 여러 번 출력해보자.

# a = int(input())
# b = input()
# print(b * a)

#-----------------------------------

# 정수 2개(a, b)를 입력받아
# a를 b번 곱한 거듭제곱을 출력하는 프로그램을 작성해보자.

# a, b = input().split()
# print(int(a)**int(b))

#-----------------------------------

# 실수 2개(f1, f2)를 입력받아
# f1을 f2번 거듭제곱한 값을 출력하는 프로그램을 작성해보자.

# a, b = input().split()
# print(float(a) ** float(b))

#-----------------------------------

# 정수 2개(a, b) 를 입력받아 a를 b로 나눈 몫을 출력해보자.

# a, b = input().split()
# print(int(a) // int(b))

#-----------------------------------
# chr( )은 정수 --> 문자 / ord( )는 문자 --> 정수로 변환하는 역할을 수행
# 단, 입력값은 문자로 받는 것을 주의

# 파이썬은 print 메소드에서 문자열에 곱하기 연산을 하면 곱한 수만큼 문장을 출력함

# 파이썬은 거듭제곱 연산자가 있다. ("**")
# 파이썬은 나누기에 몫만 구하는 연산자가 있다. ("//"), ("/")는 몫 + 나머지, ("%")는 나머지