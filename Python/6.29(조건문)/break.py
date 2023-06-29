a = int(input("숫자를 입력해주세요: "))

for i in range(1,101):
    print(i)
    if a == i:
        break # < --- break 는 하나의 for문을 빠져나갈 수 있다.
    
answer = 15
while True:
    num = int(input("숫자 맞추기 게임: "))
    if num == answer:
        print("정답~")
        break
    elif num < answer:
        print("틀렸습니다. 그것보다 더 큰 수 입니다")
    else:
        print("틀렸습니다. 그것보다 더 작은 수 입니다")
