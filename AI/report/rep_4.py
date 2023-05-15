import pandas as pd

df = pd.read_csv(r"C:\Users\gomwo\Desktop\git\python_practice\AI\report\Korean_demographics_2000-2022.csv")

filtered_df = df[(df['Date'].str.startswith('1/1/')) & (df['Region'] == 'Whole country')]

filtered_df.to_csv('whole_country.csv', index=False)