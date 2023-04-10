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
fish_target = np.array(fish_target)

index = np.arange(49)
np.random.shuffle(index)

train_data = fish_data[index[:35]]
train_target = fish_target[index[:35]]

test_data = fish_data[index[35:]]
test_target = fish_target[index[35:]]

plt.scatter(train_data[:, 0], train_data[:, 1])
plt.scatter(test_data[:, 0], test_data[:, 1])
plt.xlabel('length')
plt.ylabel('weight')
plt.show()

kn = KNeighborsClassifier()
kn.fit(train_data, train_target)
print(kn.score(test_data, test_target))
