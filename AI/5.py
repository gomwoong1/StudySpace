# 데이터 전처리

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

df = pd.read_csv(r"C:\Users\gomwoong\Desktop\git\python_practice\AI\data\Fish.csv")
df = df.loc[(df['Species'] == 'Bream') | (df['Species'] == 'Smelt')]
df = df[['Length2', 'Weight']]

fish_data = df.to_numpy()
fish_target = np.concatenate(np.ones(35), np.zeros(14))

train_input, test_input, train_target, train_input = train_test_split(
    fish_data, fish_target, stratify=fish_target, random_state=42)

