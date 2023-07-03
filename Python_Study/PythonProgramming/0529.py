from lotto import *

print('='*48)
print("■ 인하공전 컴시과 3학년 201945018 김지웅 과제물")
print("■ 사용자 모듈을 모두 가져오는 프로그램")
print('-'*48)

while True:
    value = input(">> 로또번호 추천을 시작하겠습니까? (Y/N) : ")
    print('-'*48)

    if value == 'Y' or value == 'y':
        lotto_start()
    
    elif value == 'N' or value == 'n':
        break

    else :
        print(">> 알파벳 입력 오류입니다.")
        print(">> 프로그램을 다시 시작합니다...")
        print('-'*48)

print(">> 프로그램을 종료합니다.")
print("="*48)