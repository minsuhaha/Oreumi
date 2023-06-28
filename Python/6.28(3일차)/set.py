# set 활용

'''
numbers = [1, 2, 2, 3, 3, 5]

# set으로 형변환
set_numbers = set(numbers)
print(set_numbers)
'''
a = {1, 2, 3, 5}
b = {4, 5, 6, 7}

# a&b
print(a.intersection(b))
# a|b
print(a.union(b))
# a-b
print(a.difference(b))

# 집합에서 원소 추가(add),제거(remove,discard)
a.add(4)
a.remove(5)
a.discard(5)
print(a)

# 부분집합인지 확인 (a가 b의 부분집합에 속해있다면 True)
is_sub = a.issubset(b)
print(is_sub)