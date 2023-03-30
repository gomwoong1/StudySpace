import numpy as np
import pandas as pd
import matplotlib.pyplot as mlt

fish = pd.read_csv("AI\data\Fish.csv")
print(fish.head())

fish_input = fish[['Weight', 'Length', 'Diagonal', 'Height', 'Width']].to_numpy()
fish_target = fish[['Species']].to_numpy()

