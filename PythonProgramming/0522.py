print('='*53)
print("■ 201945018 컴시과 3학년 A반 김지웅 12주차 실습")
print("■ 입력받은 구구단을 모니터와 파일에 출력하는 프로그램")
print("-"*53)
print(">> 생성할 파일명 : calfile.txt")
print(">> 생성할 경로명 : C:\Python_ex\\")
print("-"*53)

fileName = open("C:/Python_ex/calfile.txt", "w")
out_cnt = 0

while True:
    val = input(">> 프로그램을 실행하시겠습니까? (Y/N) : ")

    if val == 'y' or val == 'Y':
        out_cnt += 1

        print("-"*53)
        print(">> 구구단은 2-9 숫자만 입력하세요.")
        print("-"*53)

        while True:
            dan = int(input(">> 몇의 단을 출력할까요? : "))
            print("-"*53)
            
            if dan < 2 or dan > 9:
                print(">> 유효숫자 범위 오류!!!")
                print(">> 숫자를 다시 입력하세요...")
                print('-'*53)
                continue
            
            else :
                print(">> %d 의 구구단 출력 <<" % dan)
                txt = ">> %d 의 구구단\n" % dan
                fileName.write(txt)
                
                for i in range(1,10):
                    print("%d x %d = %d" % (dan, i, dan*i))
                    txt = "%d x %d = %d\n" % (dan, i, dan*i)
                    fileName.write(txt)
                print("-"*53)
                print(">> %d 의 단을 출력하였습니다." % dan)
                print("-"*53)
                break

    elif val == 'n' or val == 'N':
        print("-"*53)
        
        if out_cnt == 0:
            print("프로그램 실행 하지 않고 프로그램을 종료합니다.")
            pass
        else:
            print(">> 총 %d 회 반복 실행 후 프로그램을 종료합니다." % out_cnt)

        print("="*53)
        if out_cnt == 0:
            pass
        else:

            print("<<<<< 파일 쓰기 완료 >>>>>")
            print("-"*53)
            print("C:\Python_ex\\calfile.txt 파일의 내용을 확인하세요..")
            print("="*53)
        break
    
    else:
        print("-"*53)
        print(">> 알파벳을 잘못 입력하셨습니다.")
        print("-"*53)

fileName.close()