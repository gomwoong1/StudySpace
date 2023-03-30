import numpy as np
import matplotlib.pyplot as plt

class SimpleLogisticRegression():

    coef_, intercept_, y_pred = None, None, None
    z = None
    
    def sigmoid(x):
        return 1 / (1 + np.exp(-x))

    def fit(self, x_data, y_data):
        a = 0.0
        b = 0.0
        a_diff = 0
        b_diff = 0
        lr = 0.003
        epochs = 2000
        n = len(x_data)

        for i in range(epochs + 1):

            for x, y in zip(x_data, y_data):
                a_diff = x * (self.sigmoid(a * x + b) - y)
                b_diff = self.sigmoid(a * x + b) - y

                
                a = a - lr * a_diff
                b = b - lr * b_diff
                
                if i % 100 == 0:
                    print("epoch=%d, 기울기=%0.4f, 절편=%0.4f" % (i, a, b))
            
            # z = a * x_data + b 
            # self.y_pred = self.sigmoid(z)

                

x_data = np.array([[2], [4], [6], [8], [10], [12], [14]])
y_data = np.array([0, 0, 0, 1, 1, 1, 1])

slr = SimpleLogisticRegression()
slr.fit(x_data, y_data)

plt.scatter(x_data, y_data)
plt.plot(x_data, slr.y_pred)
plt.show()