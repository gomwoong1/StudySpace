import numpy as np
import matplotlib.pyplot as plt

#공부시간 X와 성적 Y의 리스트를 만듭니다.
x_data = np.array([[2], [4], [6], [8], [10], [12], [14]])
y_data = np.array([0, 0, 0, 1, 1, 1, 1])

# 기울기 a와 절편 b의 값을 초기화 합니다.
#학습률을 정합니다.
a = 0
b = 0

#시그모이드 함수를 정의합니다.
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def fit(x_data, y_data, a=0, b=0, lr=0.05, epochs=2001):
    #경사 하강법을 실행합니다.
    for i in range(epochs):
        for x, y in zip(x_data, y_data):
            a_diff = x*(sigmoid(a*x + b) - y) 
            b_diff = sigmoid(a*x + b) - y
            a = a - lr * a_diff
            b = b - lr * b_diff
            if i % 1000 == 0:    # 1000번 반복될 때마다 각 x_data값에 대한 현재의 a값, b값을 출력합니다.
                print("epoch=%.f, 기울기=%.04f, 절편=%.04f" % (i, a, b))

    return a,b

# 앞서 구한 기울기와 절편을 이용해 그래프를 그려 봅니다.
plt.scatter(x_data, y_data)

a, b = fit(x_data, y_data)

x_range = (np.arange(0, 15, 0.1)) #그래프로 나타낼 x값의 범위를 정합니다.
plt.plot(np.arange(0, 15, 0.1), np.array([sigmoid(a*x + b) for x in x_range]))
plt.show()