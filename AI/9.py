import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression

fish = pd.read_csv("AI\data\Fish.csv")
# print(fish.head())

fish_input = fish[['Weight', 'Length', 'Diagonal', 'Height', 'Width']].to_numpy()
fish_target = fish[['Species']].to_numpy()

train_input, test_input, train_target, test_target = train_test_split(
    fish_input, fish_target, random_state=42)

ss = StandardScaler()
ss.fit(train_input)
train_scaled = ss.transform(train_input)
test_scaled = ss.transform(test_input)

kn = KNeighborsClassifier(n_neighbors=3)
kn.fit(train_scaled, train_target)

print(kn.classes_)
print(kn.predict(test_scaled[:5]))

print(kn.score(train_scaled, train_target))
print(kn.score(test_scaled, test_target))

proba = kn.predict_proba(test_scaled[:5])
print(np.round(proba, decimals=4))

# bream_smelt_indexes = (train_target == 'Bream') | (train_target == 'Smelt')
# train_bream_smelt = train_scaled[bream_smelt_indexes]
# target_bream_smelt = train_target[bream_smelt_indexes]

# lr = LogisticRegression()
# lr.fit(train_bream_smelt, target_bream_smelt)

# print(lr.predict(train_bream_smelt[:5]))
# print(lr.predict_proba(train_bream_smelt[:5]))

