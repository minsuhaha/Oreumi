# NoneType
print(type(None))

# bool
print(type(True))

# 숫자형 (int, float, complex)
print(type(1))
print(type(1.2))
print(type(2 + 3j))

# 문자형
print(type('abc'))

# 시퀀스 - 순서가있는 (tuple, list)
print(type((1,2,3)))
print(type([1,2,3]))

# dict
print(type({'A':100, 'B':90, 'C':80}))

# set 집합 - 중복제거
print(type({"1", "2", "3"}))

# function
def f():
    return 1
print(type(f))