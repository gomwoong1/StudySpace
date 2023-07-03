import random

def getNumber():
    number = random.sample(range(1, 46), 6)

    return number

def lotto_start():
    fileName = open("C:/Python_ex/lotofile.txt", "w")

    print(">> 로또복권 추천번호입니다.\n")

    for i in range(1, 4):
        lotto = getNumber()
        lotto.sort()
        print("%-2d등 번호는 %s 입니다" % (i, lotto))

        tmpStr = "%02d등, %s\n" % (i, lotto)
        fileName.write(tmpStr)
    
    print("\n\n>> 김지웅님 당첨을 기원드립니다...")
    print("-"*48)

    fileName.close()
