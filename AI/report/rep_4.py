import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

VALUE = 2035

df = pd.read_csv(r"C:\Users\gomwo\Desktop\git\python_practice\AI\report\data\2039.csv")
df2 = pd.read_csv(r"C:\Users\gomwo\Desktop\git\python_practice\AI\report\data\65.csv")

tmp = df[df['region'] == 'seoul']
seoul_total = np.array(tmp['total'])

tmp = df2[df2['region'] == 'seoul']
seoul_total2 = np.array(tmp['total'])

years = np.arange(2000, 2022 + 1)
years = years.reshape(-1,1)

print(seoul_total)
print(seoul_total2)

lr = LinearRegression()
lr2 = LinearRegression()

lr.fit(years, seoul_total)
val_2039 = lr.predict([[VALUE]])
print(val_2039)

lr2.fit(years, seoul_total2)
val_65 = lr2.predict([[VALUE]])
print(val_65)

print("{}년 서울지역 소멸위험지수: {}%".format(VALUE, val_2039/val_65))