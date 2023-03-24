import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# 수면 시간에 따른 수면만족지수
# x_data = np.array([[2], [4], [6], [8]])
# y_data = np.array([45, 66, 73, 100])

x_data = np.array([[2], [4], [6], [8]])
y_data = np.array([81, 93, 91, 97])

slr = LinearRegression()
slr.fit(x_data, y_data)
slr.score(x_data, y_data)

print(slr.coef_, slr.intercept_)

# a = 8.6
a = 1.0
# b = 28.0
b = 1.0
lr = 0.01
epochs = 2000
n = len(x_data)

for i in range(epochs + 1):
    y_pred = a * x_data + b
    error = y_data - y_pred
    
    a_diff = 0
    b_diff = 0

    for j in range(n):
        a_diff += x_data[j] * (x_data[j] * a + b - y_data[j])
        b_diff += (x_data[j] * a + b - y_data[j])

    a = a - lr * a_diff
    b = b - lr * b_diff

    if i % 100 == 0:
        print("epoch=%d, 기울기=%0.4f, 절편=%0.4f" % (i, a[0], b[0]))

y_pred = a * x_data + b

plt.scatter(x_data, y_data)
plt.plot([2,8], [2*slr.coef_+slr.intercept_, 8*slr.coef_+slr.intercept_])
plt.plot(x_data, y_pred, color='yellow', linestyle='-.')
plt.show()



# y_pred = slr.predict(x_data)


# plt.plot(x_data, y_pred)


# a = 0
# b = 0

# lr = 0.03
# epochs = 2000

# for i in range(epochs+1):

# print(y_data)
# print(y_pred) # 결과값 저장


# mse = mean_squared_error(y_data, y_pred)
# print(mse)


# print(slr.coef_, slr.intercept_)
