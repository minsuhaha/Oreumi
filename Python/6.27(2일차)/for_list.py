'''
# list를 이용한 for문
fruits = ['apple', 'banana', 'grape']
for fruit in fruits:
    print(fruit)

# range -> 범위
for i in range(5):
    print(i)

# enumerate를 이용한 for문 -> index와 함께 나온다.
fruits = ['apple', 'banana', 'grape']
# idx는 int형임
for idx, x in enumerate(fruits):
    print(idx+1, x)

# zip 함수
fruits = ['apple', 'banana', 'grape']
prices = [2500, 15000, 5000]
amounts = [5, 6, 3]
for fruit, price, amount in zip(fruits, prices, amounts):
    profit = price*amount
    print(fruit, price, amount, profit)

# break 활용
for i in range(10):
    if i == 5:
        break # break는 하나의 for 문만을 빠져나감
    print(i)

# reversed
for i in reversed(range(0,10)):
    print(i)

fruits = ['apple', 'banana', 'grape']
for fruit in reversed(fruits):
    print(fruit)


# 파일 열어서 ㄹ
with open("Python/6.27(2일차)/test.txt", 'r') as f:
    text = f.read().split('\n') # 줄바꿈을 기준으로 배열을 만들어줌
    for idx, line in enumerate(text):
        name, score = line.split()
        print(f'{idx+1}번째 학생: {name}, 점수: {score}')
'''


