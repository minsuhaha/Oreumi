# tuple, list, set 서로 형변환 가능 ,tuple(), list(), set()
a =  [1, 2, 3, 3]

a = list(tuple(a))
print(a)

a = list(set(a))
print(a)