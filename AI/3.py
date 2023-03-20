# 빙어와 도미 분류하기

from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\gomwoong\Desktop\git\python_practice\AI\data\Fish.csv")
df = df.loc[(df['Species'] == 'Bream') | (df['Species'] == 'Smelt')]
df = df[['Weight', 'Length2']]

fish_data = df.to_numpy()
fish_data = np.round(fish_data, 2)
fish_target = [1] * 35 + [0] * 14

kn = KNeighborsClassifier()
kn.fit(fish_data, fish_target)
print(kn.score(fish_data, fish_target))