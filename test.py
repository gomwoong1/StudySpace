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

str = input("문자열을 입력하세요")
char = input("찾을 문자를 입력하세요")

def get_find(char, str):
    cnt = 0
    for i in range(0, len(str), 1):
        if (str[i] == char):
            return cnt
        else:
            cnt += 1
    return -1

print("결과값은", get_find(char, str), "입니다")