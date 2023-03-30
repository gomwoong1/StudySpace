import numpy as np
import matplotlib.pyplot as plt

class SimpleLogisticRegression():

    coef_, intercept_, y_pred = None, None, None
    z = None

    def fit(self, x_data, y_data):
        a = 0.0
        b = 0.0
        lr = 0.003
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
                print("epoch=%d, 기울기=%0.4f, 절편=%0.4f" % (i, a, b))

        z = a*x_data+b
        self.y_pred = 1 / (1 + np.exp(-z))
        # self.coef_ = a
        # self.intercept_ = float(np.round(b,4))
        # self.y_pred = a * x_data + b

x_data = np.array([[2], [4], [6], [8], [10], [12], [14]])
y_data = np.array([0, 0, 0, 1, 1, 1, 1])

slr = SimpleLogisticRegression()
slr.fit(x_data, y_data)

plt.scatter(x_data, y_data)
plt.plot(x_data, slr.y_pred)
plt.show()

# z = a*x_data+b
# # y = 1 / (1 + exp(-z))
# plt.scatter(x_data, y_data)
# plt.show()