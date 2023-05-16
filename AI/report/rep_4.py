import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

VALUE = 2022

region = ["seoul", "busan", "daegu", "incheon", "gwangju", "daejeon", "ulsan", "gyeonggi", "gangwon", 
        "chungcheongbukdo", "chungcheongnamdo", "jeonnabukdo", "jeonnanamdo", "gyeoungsangbukdo", 
        "gyeoungsangnamdo", "jeju"]

region_kor = ["서울", "부산", "대구", "인천", "광주", "대전", "울산", "경기도", "강원도", "충청북도",
            "충청남도", "전라북도", "전라남도", "경상북도", "경상남도", "제주"]

years = np.arange(2000, 2023)
years = years.reshape(-1,1)

df = pd.read_csv(r"C:\Users\gomwo\Desktop\git\python_practice\AI\report\data\2039.csv")
df2 = pd.read_csv(r"C:\Users\gomwo\Desktop\git\python_practice\AI\report\data\65.csv")

female_lr = LinearRegression()
old_lr = LinearRegression()

result = {}

for reg,reg_kor in zip(region, region_kor):
    tmp = df[df['region'] == reg]
    female = np.array(tmp['total'])

    tmp = df2[df2['region'] == reg]
    old = np.array(tmp['total'])

    female_lr.fit(years, female)
    old_lr.fit(years, old)

    result[reg_kor] = round(float(female_lr.predict([[VALUE]]) / old_lr.predict([[VALUE]])),2)

print("{}년 전국지역 소멸위험지수: {}%".format(VALUE, result))

