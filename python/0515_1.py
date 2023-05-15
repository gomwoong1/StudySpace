print('='*52)
print("■ 201945018 컴시과 3학년 A반 김지웅 11주차 실습")
print("■ if-else, if-elif-else 사용 파일 출력하는 프로그램")
print("-"*52)
print(">> 생성할 파일명 : testfile.txt")
print(">> 생성할 경로명 : C:\Python_ex\\")
print("-"*52)

fileName = open("C:/Python_ex/testfile.txt", "w")

jul = int(input("몇 줄 데이터를 입력할까요? : "))

for cnt in range(jul):
    hbun = input("\n\n학번을 입력하세요      : ")
    irum = input("이름을 입력하세요      : ")
    gubun = input("성별입력(남->1/여->2)  : ")
    
    if gubun == "1":
        gender = "남성"
        ki = int(input("키를 입력하세요 (cm)   : "))

        if ki >= 180:
            gugi = "농구"
        else :
            gugi = "축구"
    
    elif gubun == "2":
        gender = "여성"
        muge = int(input("체중을 입력하세요 (kg) : "))

        if muge <= 70:
            gugi = "배구"
        else :
            gugi = "피구"

    else :
        gender = "중성"
        gugi = "오류"

    score = int(input("성적을 입력하세요      : "))

    if score > 100 or score < 0:
        jumsu = "Er"
    elif score >= 95:
        jumsu = "A+"
    elif score >= 90:
        jumsu = "A"
    elif score >= 85:
        jumsu = "B+"
    elif score >= 80:
        jumsu = "B"
    elif score >= 75:
        jumsu = "C+"
    elif score >= 70:
        jumsu = "C"
    elif score >= 65:
        jumsu = "D+"
    elif score >= 60:
        jumsu = "D"
    else:
        jumsu = "F"

    val = "%02d,%12s,%5s,%3s,%3s,%3d,%3s\n" % (cnt+1, hbun, irum, gender, gugi, score, jumsu)
    fileName.write(val)

fileName.close()
print("\n<<<<< 파일 쓰기 완료 >>>>>\n")
print("-"*52)
print("C:\Python_ex\\testfile.txt 파일의 내용을 확인하세요..")
print("="*52)