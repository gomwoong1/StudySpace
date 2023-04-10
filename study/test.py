# 1

# a, b = map(int, input().split())

# if a % 2 == 0:
#     a += 1

# for i in range(a, b + 1, 2):
#     print(i)

#-----------------------------------------------------

# 2

# a = int(input())

# def is_even(a):
#     if a % 2 == 0:
#         return True
#     else:
#         return False

# if(is_even(a)):
#     print("입력값은 짝수입니다.")
# else:
#     print("입력값은 홀수입니다.")

#-----------------------------------------------------

# 3

# price = int(input())

# def cal(price):

#     # tip = price * 0.15
#     # tax = price * 0.095
#     # return price + tip + tax
#     return price + (price * 0.095) + (price * 0.15)

# total = cal(price)

# print("총 가격은", total, "원 입니다.")

#-----------------------------------------------------

# 4

# str = input()

# def get_prefix(str):
#     index = str.find("-")
#     return str[:index]

# result = get_prefix(str)
# print(result)

# -----------------------------------------------------

# 5
# str = input("문자열을 입력하세요")
# char = input("찾을 문자를 입력하세요")

# def get_find(char, str):
#     cnt = 0
#     for i in range(0, len(str), 1):
#         if (str[i] == char):
#             return cnt
#         else:
#             cnt += 1
#     return -1

# print("결과값은", get_find(char, str), "입니다")

# -----------------------------------------------------

# 6
# 주어진 리스트 안에 있는 단어 중 가장 긴 단어를 찾을 수 있도록 함수를 완성하시오.

# words = ["good", "morning", "welcome", "inhatech", "python"]

# def find_longest_word(words):
#     max = 0
#     index = 0

#     for i in range(0, len(words), 1):
#         if max < len(words[i]):
#             max = len(words[i])
#             index = i
#     return words[index]

# print("가장 긴 문자열은", find_longest_word(words), "입니다")

# -----------------------------------------------------

# 7

# 다음 국어, 영어 점수 데이터로 각 학생의 총점과 평균을 구해 출력하시오

# total = 0
# avg = 0
# import numpy as np
# kor = np.array([70,50, 70, 90])
# eng = np.array([80, 60, 90, 80])
# print((kor + eng))
# print(((kor + eng) / 2.0))

# -----------------------------------------------------

# 8
