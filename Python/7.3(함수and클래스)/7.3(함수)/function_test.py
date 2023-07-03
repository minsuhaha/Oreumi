# def greet(name):
#     print("반갑습니다! {} 여러분!".format(name))

# greet("oreumi")

# 더하기 함수
def add(a, b):
    return a+b
    
# 빼기 함수
def subtract(a, b):
    return a-b

# b에 기본값이 있는 곱하기 함수
def multiply(a, b=3):
    return a*b

# 매개변수에 *args(가변인자) -> 여러개의 매개변수 값을 받았을때 튜플 형식으로 묶어서 전체 숫자 튜플을 만들어준다.
def sum(*args):
    total = 0
    for i in args:
        total += i
    return total
result = sum(1, 2, 3, 4, 5)

def character_info(name, age):
    print("이름: ", name)
    print("나이: ", age)

result2 = character_info(name="하민수", age=20)

print(result2)