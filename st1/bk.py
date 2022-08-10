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

# 윤년 판별
# year = int(input())
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(1)
# else:
#     print(0)

# 좌표의 사분면 알아내기
# x = int(input())
# y = int(input())

# if x > 0:
#     if y > 0:
#         print(1)
#     else:
#         print(4)
# else:
#     if y > 0:
#         print(2)
#     else:
#         print(3)

# https://www.acmicpc.net/problem/2884
# hr, mn = map(int, input().split())

# if mn < 45:
#     if hr == 0:
#         hr = 23
#     else:
#         hr -= 1
#     mn += 15
# else:
#     mn -= 45

# print(hr,mn)

# https://www.acmicpc.net/problem/2525
# hr, mn = map(int, input().split())
# tm = int(input())

# if mn >= 60 - tm:
#     hr += tm // 60
#     mn += tm % 60
# else:
#     mn += tm

# if mn >= 60:
#     hr += 1
#     mn -= 60
# if hr >= 24:
#     hr -= 24

# print(hr,mn)


# https://www.acmicpc.net/problem/2480

# in_list = list(map(int,input().split()))
# bigger = 0

# if in_list[0] == in_list[1] == in_list[2]:
#     print(10000+(in_list[0]*1000))
# elif in_list[0] == in_list[1]:
#     print(1000+(in_list[0]*100))
# elif in_list[0] == in_list[2]:
#     print(1000+(in_list[0]*100))
# elif in_list[1] == in_list[2]:
#     print(1000+(in_list[1]*100))
# else:
#     for i in in_list:
#         if i > bigger:
#             bigger = i
#     print(bigger*100)

# https://www.acmicpc.net/problem/3003

# kn, qe, lk, bs, nt, ph = map(int, input().split())
# print(1-kn, 1-qe, 2-lk, 2-bs, 2-nt, 8-ph)

# 입력받은 정수의 구구단을 출력
# a = int(input())
# for b in range(1,10):
#     print('{} * {} = {}'.format(a, b, a*b))

# https://www.acmicpc.net/problem/10950
num = int(input())

for _ in range(num):
    a, b = map(int,input().split())
    print(a+b)