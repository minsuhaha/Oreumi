# for i in range(1, 11):
#     if i == 5:
#         pass # < -- 단순히 그냥 넘기기 (비워두기 용)
#     else:
#         print("하이")

a = [2, 1, 3, 4, 6, 7, 5]
# 방법1
res = a[0]
for i in range(1, len(a)):
    if a[i] > a[i-1]:
        res = a[i]
print(res)

# 방법2
max = a[0]
for i in a:
    if max < i:
        max = i
print(max)


