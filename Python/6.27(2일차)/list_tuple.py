a = [1, '1', True, None, [1,2]]
b = (1, '1', True, None, [1,2])

# 리스트는 변경 가능 (mutable)
a[1] = False
print(a)

# 튜플은 변경 불가 (immutable)
b[1] = False
print(b)