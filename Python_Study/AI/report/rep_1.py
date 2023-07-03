# 외부 라이브러리 import
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error

# 클래스 정의
class SimpleLinearRegression():

    # 기울기, 예측값, 저장저장할 변수 선언
    coef_, intercept_, y_pred = None, None, None

    def fit(self, x_data, y_data):
        # 경사하강법을 위한 초기값 설정
        # 기울기와 절편은 각각 1.0, 학습율은 0.01, 반복회수는 2000번으로 설정
        # 데이터의 개수를 n에 저장
        a = 0.0
        b = 0.0
        lr = 0.03
        epochs = 2000
        n = len(x_data)

        # 경사하강법 수행
        for i in range(epochs + 1):
            y_pred = a * x_data + b
            
            # 기울기, 절편의 누적 차이값 저장 변수
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

        # 경사하강법 종료 후 기울기, 절편, 예측값을 각 인스턴스 변수에 저장
        self.coef_ = a
        self.intercept_ = float(np.round(b,4))
        self.y_pred = a * x_data + b

    def predict(self, X):
        pred = np.dot(X, self.coef_) + self.intercept_
        return pred

    def score(self, x, y):
        y_pred = self.predict(x) # 예측값
        y_mean = np.mean(y) # y 데이터 평균값
        ssr = np.sum((y - y_pred)**2) # y에서 y의 예측값을 뺀 결과의 총합
        sst = np.sum((y - y_mean)**2) # y에서 y의 평균값을 뺀 결과의 총합
        r2_score = 1 - (ssr / sst) # R2 Score 공식을 이용해 값 계산
        return r2_score

# x, y 데이터를 넘파이 배열로 선언
x_data = np.array([[1], [2], [3], [4]])
y_data = np.array([2, 5, 7, 9])

# 객체 생성, fit() 함수 호출
slr = SimpleLinearRegression()
slr.fit(x_data, y_data)

# 기울기, 절편 및 예측값과 점수 출력
print(slr.coef_, slr.intercept_)
print(slr.predict([[5]]))
print(slr.score(x_data, y_data))

# 산점도 그래프를 통해 x, y 데이터를 시각화
plt.scatter(x_data, y_data)

# 선그래프로 기울기와 절편을 시각화
plt.plot(x_data, slr.y_pred)
plt.show()