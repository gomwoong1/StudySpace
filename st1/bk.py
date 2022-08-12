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
# num = int(input())

# for _ in range(num):
#     a, b = map(int,input().split())
#     print(a+b)

# 1부터 n까지 합을 출력한다.
# sum = 0
# for i in range(1,int(input())+1):
#     sum += i
# print(sum)

# 영수증 검증
# sum = 0
# price = int(input())
# for _ in range(int(input())):
#     pri, count = map(int, input().split())
#     sum += pri*count
# if sum == price:
#     print('Yes')
# else:
#     print('No')

# https://www.acmicpc.net/problem/15552
# import sys
# for _ in range(int(input())):
#     a, b = map(int, sys.stdin.readline().split())
#     print(a+b)

# 좀 더 이쁘게 출력
# import sys
# for i in range(int(input())):
#     a, b = map(int, sys.stdin.readline().split())
#     print('Case #{}: {}'.format(i+1, a+b))

# 좀 좀 더 이쁘게 출력
# import sys
# for i in range(int(input())):
#     a, b = map(int, sys.stdin.readline().split())
#     print('Case #{}: {} + {} = {}'.format(i+1, a, b, a+b))

# 별 찍기
# for i in range(1,int(input())+1):
#     print('*'*i)

# 오른쪽 정렬하여 별 찍기
# max = int(input())
# for i in range(1, max+1):
#     str = '*'*i
#     print(str.rjust(max))

# https://www.acmicpc.net/problem/10871
# import sys
# print_list = []
# max, num = map(int, input().split())
# list = list(map(int, sys.stdin.readline().split()))

# for i in list:
#     if i < num:
#         print_list.append(i)
# print(*print_list)

# 0 0이 들어올 때까지 A+B를 출력하는 문제
# while True:
#     a, b = map(int, input().split())
#     if a == 0 and b == 0:
#         break
#     else:
#         print(a+b)

# 입력이 끝날 때까지 A+B를 출력하는 문제. EOF에 대해 알아 보세요
# while True:
#     try:
#         a, b = map(int, input().split())
#         print(a+b)
#     except:
#         break

# 원래 수로 돌아올 때까지 연산을 반복하는 문제
# count = 1
# val = input()
# val2 = ''
# next_num = ''

# if len(val) == 1:
#     val2 = val.zfill(2)
#     val = val2
# else:
#     val2 = val

# while True:
#     next_num = str(int(val2[0])+int(val2[1]))
#     if len(next_num) == 2:
#         next_num = next_num[1]
#     if val2[1]+next_num == val:
#         break
#     else:
#         count += 1
#         val2 = val2[1]+next_num

# print(count)

# in_val = int(input())
# cnt = 0
# num = in_val

# while True:
#     a = num // 10
#     b = num % 10
#     c = (a+b) % 10
#     num = (b*10)+c
#     cnt += 1
#     if num == in_val:
#         break
# print(cnt)

# 최대, 최소값 구하기
# maxi = 1
# mini = 1000000

# val = int(input())
# nums = list(map(int,input().split()))

# for i in nums:
#     if i > maxi:
#         maxi = i
#     if i < mini:
#         mini = i
# print(mini,maxi)

# val = int(input())
# nums = list(map(int,input().split()))
# print(min(nums),max(nums))

# 최대값과 위치 구하기
# nums = []
# for _ in range(9):
#     nums.append(int(input()))
# print(max(nums))
# print(nums.index(max(nums))+1)

# 서로 다른 나머지 구하기
# nums = []
# result = []

# for _ in range(10):
#     nums.append(int(input())%42)

# for i in nums:
#     if i not in result:
#         result.append(i)
# print(len(result))

# nums = []

# for _ in range(10):
#     a = int(input())%42
#     if a not in nums:
#         nums.append(a)

# print(len(nums))

# 성적 조작
# sum = 0
# val = int(input())
# nums = list(map(int,input().split()))

# for i in nums:
#     sum += i/max(nums)*100
# print(sum/val)

# OX 퀴즈의 결과를 일차원 배열로 입력받아 점수를 계산하는 문제
# val = int(input())

# for _ in range(val):
#     score = 0
#     total = 0
#     nums = list(input())
#     for i in nums:
#         if i == 'O':
#             score += 1
#             total += score
#         else:
#             score = 0
#     print(total)

# https://www.acmicpc.net/problem/4344

# val = int(input())
# for _ in range(val):
#     avg = 0
#     per = 0
#     nums = list(map(int,input().split()))
#     avg = sum(nums[1:])/nums[0]
#     for i in nums[1:]:
#         if i > avg:
#             per += 1
#     per = per/nums[0]*100

#     print('{:.3f}%'.format(per))

# https://www.acmicpc.net/problem/15596
# sum = 0
# def solve(a):
#     val = 0
#     for i in a:
#         val += i
#     return val

# nums = list(map(int,input().split()))
# sum = solve(nums)

# 문자를 아스키코드로 변환
# print(ord(input()))

# https://www.acmicpc.net/problem/11720
# val = int(input())
# nums = list(map(int,input()))
# print(sum(nums))

# 한 단어에서 각 알파벳이 처음 등장하는 위치를 찾는 문제
# nums = []

# string = list(map(ord,input()))
# for i in range(97, 123):
#     try:
#         if string.index(i) <= 100:
#             nums.append(string.index(i))
#     except:
#         nums.append(-1)
# print(*nums)

# https://www.acmicpc.net/problem/2675
# import sys

# for _ in range(int(sys.stdin.readline())):
#     string =''
#     val, in_list = input().split()
#     for i in in_list:
#         string += i*int(val)
#     print(string)

# 주어진 단어에서 가장 많이 사용된 알파벳을 출력하는 문제

# import sys
# string = list(sys.stdin.readline().upper())
# count2 = 0
# char = ''

# for i in range(65, 91):
#     if chr(i) in string:
#         count = 0
#         count += string.count(chr(i))
#         if count > count2:
#             char = chr(i)
#             count2 = count
#         elif count == count2:
#             char = '?'
# print(char)

# 단어의 개수를 구하는 문제
# import sys
# string = list(sys.stdin.readline().split())
# print(len(string))

