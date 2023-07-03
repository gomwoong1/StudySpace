import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

class peopleRegression:
    region = ["seoul", "busan", "daegu", "incheon", "gwangju", "daejeon", "ulsan", "gyeonggi", "gangwon", 
        "chungcheongbukdo", "chungcheongnamdo", "jeonnabukdo", "jeonnanamdo", "gyeoungsangbukdo", 
        "gyeoungsangnamdo", "jeju"]

    region_kor = ["서울", "부산", "대구", "인천", "광주", "대전", "울산", "경기도", "강원도", "충청북도",
            "충청남도", "전라북도", "전라남도", "경상북도", "경상남도", "제주"]
    
    df = None
    df2 = None
    years = None
    result = {}
    female_lr = LinearRegression()
    old_lr = LinearRegression()

    def __init__(self):
        self.df = pd.read_csv(r"C:\Users\gomwo\Desktop\git\python_practice\AI\report\data\2039.csv")
        self.df2 = pd.read_csv(r"C:\Users\gomwo\Desktop\git\python_practice\AI\report\data\65.csv")

        self.years = np.arange(2000, 2023)
        self.years = self.years.reshape(-1,1)

    def predict(self, value):
        for reg,reg_kor in zip(self.region, self.region_kor):
            tmp = self.df[self.df['region'] == reg]
            female = np.array(tmp['total'])

            tmp = self.df2[self.df2['region'] == reg]
            old = np.array(tmp['total'])

            self.female_lr.fit(self.years, female)
            self.old_lr.fit(self.years, old)

            self.result[reg_kor] = round(float(self.female_lr.predict([[value]]) / self.old_lr.predict([[value]])),2)
        
        return self.result