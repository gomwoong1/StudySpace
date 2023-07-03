import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

df = pd.read_csv(r"C:\Users\gomwo\Desktop\git\python_practice\AI\report\data\2039.csv")
df2 = pd.read_csv(r"C:\Users\gomwo\Desktop\git\python_practice\AI\report\data\65.csv")

female_lr = LinearRegression()
old_lr = LinearRegression()

years = np.arange(2000, 2023)
years = years.reshape(-1,1)

tmp = df[df['region'] == 'seoul']
female = np.array(tmp['total'])

tmp = df2[df2['region'] == 'seoul']
old = np.array(tmp['total'])

female_lr.fit(years, female)
old_lr.fit(years, old)

print("여성인구 예측모델 R2 Score:", female_lr.score(years, female))
print("노령인구 예측모델 R2 Score:", old_lr.score(years, old))

plt.scatter(years, female)
plt.scatter(years, old)
plt.show()