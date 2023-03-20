# 테스트 데이터와 훈련 데이터 나누기

from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\gomwoong\Desktop\git\python_practice\AI\data\Fish.csv")
df = df.loc[(df['Species'] == 'Bream') | (df['Species'] == 'Smelt')]
df = df[['Length2', 'Weight']]

fish_data = df.to_numpy()
fish_data = np.round(fish_data, 2)
fish_target = [1] * 35 + [0] * 14

train_data = fish_data[:35]
train_target = fish_target[:35]

test_data = fish_data[35:]
test_target = fish_target[35:]

kn = KNeighborsClassifier()
kn.fit(train_data, train_target)
kn.score(test_data, test_target)
