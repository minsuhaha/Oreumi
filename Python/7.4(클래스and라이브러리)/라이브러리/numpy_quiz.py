import numpy as np

a = [10, 24, 32, 40, 3]
b = [5, 7, 14, 23, 32]

# 1. numpy를 이용해 리스트 a의 평균, 전체 합 구하기
# 평균 구하기
mean = np.mean(a)
print(mean)

# 합 구하기
sum = np.sum(a)
print(sum)

# 2. numpy의 array를 이용하여 a, b 벡터 합, 차 이용해보기(각 원소들의 합한 리스트 출력 = [15, 31, 46, 63, 35]  )
a = np.array(a)
b = np.array(b)

# a, b 백터의 합
sum = a + b
print(sum)

# a, b 백터의 차
substract = a - b
print(substract)

