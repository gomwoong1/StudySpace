# 외부 라이브러리 import
import numpy as np
import matplotlib.pyplot as plt

# 클래스 정의
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

    # 경사 하강법을 통해 최적의 a, b 값을 찾기
    def fit(self, x_data, y_data, a=0, b=0, lr=0.05, epochs=2001):
        for i in range(epochs):
            for x, y in zip(x_data, y_data):
                z = self.sigmoid(a*x+b)

                a_diff = x*(z - y) 
                b_diff = z - y

                a = a - lr * a_diff
                b = b - lr * b_diff

                # 1000번 반복될 때마다 각 x_data값에 대한 현재의 a값, b값을 출력
                if i % 1000 == 0:    
                    print("epoch=%.f, 기울기=%.04f, 절편=%.04f" % (i, a, b))

        self.set_a(a)
        self.set_b(b)

    def predict(self, x_data):
        # 샘플 데이터를 시그모이드 함수로 연산 후 판별
        # 0.5보다 높으면 1(합격), 낮으면 0(불합격)
        prob = self.sigmoid(self.a*x_data + self.b)
        return np.where(prob>= 0.5, 1, 0)

    def score(self, x_data, y_data):
        # predict를 통해 결과값을 반환
        # 결과값은 2차원 배열로 반환되기 때문에 reshape로 1차원 배열로 변경
        y_pred = self.predict(x_data).reshape(len(y_data))

        # 예측값과 y데이터가 몇 개 같은지 비교 후 y 데이터 개수만큼 나눠 정확도 계산
        accuracy = np.sum(y_pred == y_data) / len(y_data)

        return accuracy


# 공부시간 x와 성적 y의 데이터를 담은 넘파이 배열을 생성
x_data = np.array([[2], [4], [6], [8], [10], [12], [14]])
y_data = np.array([0, 0, 0, 1, 1, 1, 1])

# 데이터 시각화
plt.scatter(x_data, y_data)

slr = SimpleLogisticRegression()
slr.fit(x_data, y_data)

# x값의 범위를 정함
x_range = (np.arange(0, 15, 0.1)) 

# x값에 따른 시그모이드 곡선을 시각화
plt.plot(x_range, np.array([slr.sigmoid(slr.a*x + slr.b) for x in x_range]))
plt.show()

# 예측 및 정확도 출력하기
print(slr.predict([[6.7], [8]]))
print(slr.score(x_data, y_data))