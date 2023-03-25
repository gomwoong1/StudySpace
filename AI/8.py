import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures

df = pd.read_csv('AI\data\perch_full.csv')
perch_full = df.to_numpy()

print(perch_full)

# 다항 회귀 객체 생성
# degree = 2는 기본값으로, 다항식의 차수를 설정
# 기본값이 거듭제곱임
poly = PolynomialFeatures()

poly.fit([[2,3]])

print(poly.transform([[2, 3]]))

poly = PolynomialFeatures(include_bias=False)

