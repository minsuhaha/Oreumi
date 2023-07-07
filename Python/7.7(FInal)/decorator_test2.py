# def caculation(func):
#     def wrapper(*args, **kwargs):
#         print("데코레이터1 시작")  # --> 1
#         func(*args, **kwargs)  # --> caculation 2까지 종료
#         print("데코레이터1 종료") # --> 5
#     return wrapper

# def caculation2(func):
#     def wrapper(*args, **kwargs):
#         print("데코레이터2 시작") # --> 2
#         func(*args, **kwargs)
#         print("데코레이터2 종료") # --> 4
#     return wrapper

# # 액자식 구조
# @caculation
# @caculation2
# def add(a, b):
#     print(a + b) # --> 3

# add(3, 5)

def start_calculation(func):
    def wrapper(*args, **kwargs):
        print("아래 결과는?")
        value = func(*args, **kwargs)
        print("%0.2f" % value)
    return wrapper

@start_calculation
def divide(a, b):
       print(f"{a}를 {b}로 나누겠습니다.")
       return  a / b

divide(7, 3)

# 아래 결과는?
# 7를 3로 나누겠습니다.
# 2.33