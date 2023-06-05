from ex_09_10_11 import *

print('='*48)
print("■ 인하공전 컴시과 1학년 202345011 이유진 과제물")
print("■ 사용자 모듈을 모두 가져오는 프로그램")
print('-'*48)

while True:
    check = input(">> 로또번호 추천을 시작하겠습니까? (Y/N) : ")
    print('-'*48)

    if check == 'y' or check == 'Y':
        lotto_start()
    
    elif check == 'n' or check == 'N':
        break

    else :
        print(">> 알파벳 입력 오류입니다.")
        print(">> 프로그램을 다시 시작합니다...")
        print('-'*48)

print(">> 프로그램을 종료합니다.")
print("="*48)