import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

df = pd.read_csv(r"C:\Users\gomwo\Desktop\git\python_practice\AI\report\2039.csv")

seoul = df[df['region'] == 'seoul']
seoul_total_values = np.array(seoul['total'])

years = np.arange(2000, 2022 + 1)
years = years.reshape(-1,1)

print(seoul_total_values)

lr = LinearRegression()

lr.fit(years, seoul_total_values)
print(lr.predict([[2039]]))