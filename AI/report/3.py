import numpy as np
import matplotlib.pyplot as plt

class SimpleLogisticRegression:
    # 기울기, 절편값을 저장할 변수를 선언
    a, b = None, None

    # a값 setter
    def set_a(self, a):
        self.a = a

    # b값 setter
    def set_b(self, b):
        self.b = b

    # 시그모이드 함수 정의
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def fit(self, x_data, y_data, a=0, b=0, lr=0.05, epochs=2001):
        # 경사 하강법을 통해 최적의 a, b 값을 찾기
        for i in range(epochs):
            for x, y in zip(x_data, y_data):
                z = self.sigmoid(a*x+b)

                a_diff = x*(z - y) 
                b_diff = z - y

                a = a - lr * a_diff
                b = b - lr * b_diff
                if i % 1000 == 0:    # 1000번 반복될 때마다 각 x_data값에 대한 현재의 a값, b값을 출력
                    print("epoch=%.f, 기울기=%.04f, 절편=%.04f" % (i, a, b))

        self.set_a(a)
        self.set_b(b)

    def predict(self, x_data):
        # 샘플 데이터를 시그모이드 함수로 연산 후 판별
        # 0.5보다 높으면 1(합격), 낮으면 0(불합격)
        prob = self.sigmoid(self.a*x_data + self.b)
        return np.where(prob>= 0.5, "합격", "불합격")

    def score(self):
        pass


#공부시간 X와 성적 Y의 리스트를 만듭니다.
x_data = np.array([[2], [4], [6], [8], [10], [12], [14]])
y_data = np.array([0, 0, 0, 1, 1, 1, 1])

# 앞서 구한 기울기와 절편을 이용해 그래프를 그려 봅니다.
plt.scatter(x_data, y_data)

slr = SimpleLogisticRegression()
slr.fit(x_data, y_data)

x_range = (np.arange(0, 15, 0.1)) #그래프로 나타낼 x값의 범위를 정합니다.
plt.plot(x_range, np.array([slr.sigmoid(slr.a*x + slr.b) for x in x_range]))
plt.show()

print(slr.predict([[6.8], [8]]))