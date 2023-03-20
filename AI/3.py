# 빙어와 도미 분류하기

from sklearn.neighbors import KNeighborsClassifier

import pandas as pd

fish = pd.read_csv("/data/Fish.csv")
print(fish)

# kn = KNeighborsClassifier()

# kn.fit(fish_data, fish_target)