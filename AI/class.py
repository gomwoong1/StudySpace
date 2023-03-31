import random

grade_1 = ['현아', '유진', ' 민성', '태균', '보현', '형근', '혜진', '서림',
    '지원', '재균', '민정', '관용', '동욱', '한울', '희주', '창욱', '민호', '혁주']

depart = []

for i in range(6):
    tmp = []
    for j in range(3):
        random.shuffle(grade_1)
        tmp.append(grade_1.pop())
    depart.append(tmp)

print(depart)