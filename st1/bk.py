# Hello World!를 출력하시오.
# print('Hello World!')


# 두 줄에 걸쳐 "강한친구 대한육군"을 한 줄에 한 번씩 출력한다.
# print('강한친구 대한육군')
# print('강한친구 대한육군')

# 고양이를 출력한다.
# print('''\\    /\\''')
# print(' )  ( \')')
# print('(  /  )')
# print(' \\(__)|')

# 개를 출력한다.
# dog = '''|\\_/|
# |q p|   /}
# ( 0 )"""\\
# |"^"`    |
# ||_/=\\\\__|'''
# print(dog)

# 첫째 줄에 A+B를 출력한다.
# a, b = input().split()
# print(int(a)+int(b))

# 첫째 줄에 A-B를 출력한다.
# a, b = input().split()
# print(int(a)-int(b))

# 첫째 줄에 A×B를 출력한다.
# a, b = map(int, input().split())
# print(a*b)

# 첫째 줄에 A/B를 출력한다
# a, b = map(int, input().split())
# print(a/b)

# 첫째 줄에 A+B, 둘째 줄에 A-B, 셋째 줄에 A*B, 넷째 줄에 A/B, 다섯째 줄에 A%B를 출력한다.
# a, b = map(int, input().split())
# print(a+b)
# print(a-b)
# print(a*b)
# print(a//b)
# print(a%b)

# 첫째 줄에 준하가 가입하려고 하는 사이트에 이미 존재하는 아이디가 주어진다. 
# 첫째 줄에 준하의 놀람을 출력한다. 놀람은 아이디 뒤에 ??!를 붙여서 나타낸다.
# id = str(input())
# print(id+'??!')

# 불기 연도를 서기 연도로 변환한 결과를 출력한다.
# year = int(input())
# print(year-543)

# 첫째 줄에 (A+B)%C, 둘째 줄에 ((A%C) + (B%C))%C, 셋째 줄에 (A×B)%C, 넷째 줄에 ((A%C) × (B%C))%C를 출력한다
# a, b, c = map(int, input().split())
# print((a+b)%c)
# print(((a%c)+(b%c))%c)
# print((a*b)%c)
# print(((a%c)*(b%c))%c)

# https://www.acmicpc.net/problem/2588
# a = int(input())
# b = int(input())
# print(a*(b%10))
# print(a*int((b/10)%10))
# print(a*(b//100))
# print(a*b)

# 새싹을 출력한다.
# plant = """         ,r'"7
# r`-_   ,'  ,/
#  \\. ". L_r'
#    `~\\/
#       |
#       |"""
# print(plant)

# https://www.acmicpc.net/problem/1330
# a, b = map(int, input().split())
# if a > b:
#     print('>')
# elif a == b:
#     print('==')
# else:
#     print('<')

# 시험 성적을 출력한다.
# score = int(input())
# if score >= 90:
#     print('A')
# elif score >= 80:
#     print('B')
# elif score >= 70:
#     print('C')
# elif score >= 60:
#     print('D')
# else:
#     print('F')
