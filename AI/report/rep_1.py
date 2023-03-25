import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

x_data = np.array([[1], [2], [3], [4]])
y_data = np.array([2, 5, 7, 9])

slr = LinearRegression()
slr.fit(x_data, y_data)

a = 1.0
b = 1.0
lr = 0.01
epochs = 2000
n = len(x_data)

for i in range(epochs + 1):
    y_pred = a * x_data + b
    
    a_diff = 0
    b_diff = 0

    for j in range(n):
        a_diff += x_data[j] * (x_data[j] * a + b - y_data[j])
        b_diff += (x_data[j] * a + b - y_data[j])

    a = a - lr * a_diff
    b = b - lr * b_diff

    if i % 100 == 0:
        mse = mean_squared_error(y_data, y_pred)
        print("epoch=%d, 기울기=%0.4f, 절편=%0.4f, MSE: %0.2f" % (i, a, b, mse))

y_pred = a * x_data + b

slr_a = slr.coef_
slr_b = slr.intercept_

print("R2 Score:", slr.score(x_data, y_data))
print(slr.predict( [[5]]))
print("기울기:", slr_a, "절편:", slr_b)

plt.scatter(x_data, y_data)
plt.plot(x_data, slr_a * x_data + slr_b, color='black')
plt.plot(x_data, y_pred, color='yellow', linestyle='--')
plt.show()