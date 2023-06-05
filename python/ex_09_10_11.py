import random

def getNumber():
    number = random.sample(range(1, 46), 6)

    return number

def lotto_start():
    fileName = open("C:/Python_ex/lotofile.txt", "w")

    print(">> 로또복권 추천번호입니다.\n")

    for i in range(1, 4):
        number = getNumber()
        number.sort()
        print("%-2d등 번호는 %s 입니다" % (i, number))

        str = "%02d등, %s\n" % (i, number)
        fileName.write(str)
    
    print("\n\n>> 이유진님 당첨을 기원드립니다...")
    print("-"*48)

    fileName.close()
