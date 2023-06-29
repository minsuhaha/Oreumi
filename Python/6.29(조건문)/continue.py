for i in range(1, 101):
    if i > 50:
        print("50보다 큽니다")
        continue # <- continue를 만나고 난 뒤 뒤에 구문은 실행되지 않고 다시 for 반복문으로 ㄱㄱ
    print("50보다 같거나 작습니다")
