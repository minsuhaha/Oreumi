# 일급함수
'''
def cat():
    return "Meow"

my_favorite_animal = cat

print(my_favorite_animal())
'''

# 고차함수 -> 매개변수안에 함수 입력받기
'''
def apply_operation(func, *args):
    return func(args)
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a*b

result = apply_operation(multiply, 2, 3) # 함수를 인자로 전달하여 실행
print(result)
'''
