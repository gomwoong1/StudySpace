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
            for x_data, y_data in data:
                a_diff = x_data * (self.sigmoid(a * x_data + b) - y_data)
                b_diff = self.sigmoid(a * x_data + b) - y_data
                
                a = a - lr * a_diff
                b = b - lr * b_diff
                
                if i % 100 == 0:
                    print("epoch=%d, 기울기=%0.4f, 절편=%0.4f" % (i, a, b))
            
            # z = a * x_data + b 
            # self.y_pred = self.sigmoid(z)

                

# x_data = np.array([[2], [4], [6], [8], [10], [12], [14]])
# y_data = np.array([0, 0, 0, 1, 1, 1, 1])
data = [[2, 0], [4, 0], [6, 0], [8, 1], [10, 1], [12, 1], [14, 1]]

slr = SimpleLogisticRegression()
slr.fit([i[0] for i in data], [i[1] for i in data])

plt.scatter([i[0] for i in data], [i[1] for i in data])
# plt.plot(x_data, slr.y_pred)
# plt.show()