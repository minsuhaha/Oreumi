n = int(input())
curr, next = 0, 1
res = 1
for i in range(2, n+1):
    res = curr + next
    curr, next = next, res
print(res)


