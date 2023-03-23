import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# 수면 시간에 따른 수면만족지수
x_data = np.array([[2], [4], [6], [8]])
y_data = np.array([45, 66, 73, 100])

slr = LinearRegression()
slr.fit(x_data, y_data)
slr.score(x_data, y_data)

y_pred = slr.predict(x_data)

plt.scatter(x_data, y_data)
plt.plot(x_data, y_pred)
plt.show()

a = 0
b = 0

lr = 0.03
epochs = 2000



# mse = mean_squared_error(y_data, y_pred)
# print(mse)
# print(slr.coef_, slr.intercept_)
