import pandas as pd

df = pd.read_csv(r"C:\Users\gomwo\Desktop\git\python_practice\capstone\QnA_1499.csv")

print(len(df))
print(df.head())

df = df.dropna(subset=['answer'])

print(len(df))
print(df.head())

df.to_csv('test.csv', encoding='utf-8-sig', index=False)