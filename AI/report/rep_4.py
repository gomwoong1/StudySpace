import pandas as pd

df = pd.read_csv(r"C:\Users\gomwo\Desktop\git\python_practice\AI\report\Korean_demographics_2000-2022.csv")

filtered_df = df[df['Region'] == 'Whole country']
print(filtered_df)