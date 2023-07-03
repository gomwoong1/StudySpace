print('='*52)
print("■ 201945018 컴시과 3학년 A반 김지웅 12주차 실습")
print("■ 입력받은 구구단을 모니터와 파일에 출력하는 프로그램")
print("-"*52)
print(">> 생성할 파일명 : calfile.txt")
print(">> 생성할 경로명 : C:\Python_ex\\")
print("-"*52)

fileName = open("C:/Python_ex/calfile.txt", "w")

val = input(">>프로그램을 실행하시겠습니까? (Y/N) : ")

while(val == "y" or val == "Y"):
    print("-"*52)
    print(">> 구구단은 2-9 숫자만 입력하세요.")
    print("-"*52)
    dan = int(input(">> 몇의 단을 출력할까요? : "))
    print("-"*52)
    
    print(">> %d 의 구구단 출력 <<" % dan)
    txt = ">> %d 의 구구단\n" % dan
    fileName.write(txt)
    
    for i in range(1,10):
        print("%d x %d = %d" % (dan, i, dan*i))
        txt = "%d x %d = %d\n" % (dan, i, dan*i)
        fileName.write(val)

    print(">> %d 의 단을 출력하였습니다." % dan)
    print("-"*52)
    val = input(">>프로그램을 실행하시겠습니까? (Y/N) : ")

# fileName.close()