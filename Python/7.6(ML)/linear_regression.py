import numpy as np
from sklearn.linear_model import LinearRegression

X = np.array([[30], [40], [50], [60], [70]])

Y = np.array([100, 150, 200, 250, 300])

# LinearRegression model 만들어주기
model = LinearRegression()

# 독립변수, 종속변수 LinearRegression 모델로 학습시키기
model.fit(X, Y)

size = int(input("주택평수입력?"))
house_size = np.array([[size]])

# 새로운 값에 대해 학습된 모델을 이용하여 예측
predicted_price = model.predict(house_size)
print(f"{size}평수의 예측금액은?", predicted_price)