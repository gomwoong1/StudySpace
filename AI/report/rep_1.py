# 외부 라이브러리 import
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

class SimpleLinearRegression():

    # 기울기, 예측값, 저장저장할 변수 선언 및 초기화
    coef_, intercept_, y_pred = 0.0, 0.0, 0.0

    # 선형회귀 모델 생성 및 x, y 데이터 학습
    slr = LinearRegression()
    
    def fit(self, x_data, y_data):
        # 경사하강법을 위한 초기값 설정
        # 기울기와 절편은 각각 1.0, 학습율은 0.01, 반복회수는 2000번으로 지정
        # 데이터의 개수를 n에 저장
        a = 1.0
        b = 1.0
        lr = 0.05
        epochs = 2000
        n = len(x_data)

        # 경사하강법 수행
        for i in range(epochs + 1):
            y_pred = a * x_data + b
            
            a_diff = 0
            b_diff = 0

            # 기울기와 절편에 대한 비용함수의 편미분 값을 계산하여 누적
            for j in range(n):
                a_diff += x_data[j] * (x_data[j] * a + b - y_data[j])
                b_diff += (x_data[j] * a + b - y_data[j])

            # 이전 a,b의 값 - 학습률과 누적된 차이값을 곱한값을 연산
            # 값을 업데이트 하여 a, b 값을 최적화
            a = a - lr * a_diff
            b = b - lr * b_diff

            # 반복회수가 100의 배수일 때마다 기울기, 절편, MSE값 출력
            if i % 100 == 0:
                mse = mean_squared_error(y_data, y_pred)
                print("epoch=%d, 기울기=%0.4f, 절편=%0.4f, MSE: %0.2f" % (i, a, b, mse))

            # 경사하강법을 통해 찾은 기울기, 절변, 예측값을 저장
            self.coef_ = a
            self.intercept_ = b
            self.y_pred = a * x_data + b
            


# # 산점도 그래프를 통해 x, y 데이터를 시각화
# plt.scatter(x_data, y_data)

# # 모델이 찾은 기울기와 절편을 시각화
# # 경사하강법을 통해 찾은 기울기와 절편을 시각화
# plt.plot(x_data, slr_a * x_data + slr_b, color='black')
# plt.plot(x_data, y_pred, color='yellow', linestyle='--')
# plt.show()

# x, y 데이터를 넘파이 배열로 선언
x_data = np.array([[1], [2], [3], [4]])
y_data = np.array([2, 5, 7, 9])

lr = SimpleLinearRegression()
lr.fit(x_data, y_data)
print(lr.coef_, lr.intercept_, lr.y_pred)