# 백준 별찍기 알고리즘 풀이

'''
# 문제 1. 별찍기 - 1
이중 for문을 이용하여 별찍기
n = int(input())
for i in range(1, n+1):
    for j in range(i):
        print('*', end='')
    print()

for문 하나만 쓰기
n = int(input())
for i in range(1, n+1):
    print('*' * i)


# 문제 2. 별찍기 - 2
n = int(input())
for i in range(1, n+1):
    print(' '*(n-i) + '*'*i)


# 문제 3. 별찍기 - 3
n = int(input())
for i in reversed(range(1, n+1)):
    print('*' * i)


# 문제 4. 별찍기 - 4
n = int(input())
for i in range(n, 0, -1):
    print(' '*(n-i) + '*'*i)


# 문제 12. 별찍기 - 12
n = int(input())
for i in range(1, n*2):
    if i <= n:
        print(' '*(n-i)+'*'*i)
    else:
        print(' '*(i-n)+'*'*(n*2-i))

# 문제 13. 별찍기 - 13
n = int(input())
for i in range(1, n*2):
    if i <= n:
        print('*'*i)
    else:
        print('*'*(n*2-i))
'''    
