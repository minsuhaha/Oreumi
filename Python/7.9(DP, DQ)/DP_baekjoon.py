# def fib(n):
#     if n==1 or n==2:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
        
# def fibonacci(n):
#     dp=[0]*(n+1)
#     dp[1],dp[2]=1,1
#     cnt2=0
#     for i in range(3,n+1):
#         cnt2+=1
#         dp[i]=dp[i-1]+dp[i-2]
#     return dp[n], cnt2


# n = int(input())
# count, count2 = fibonacci(n)
# print(count, count2)

# 1904번. 01 타일 1
'''
n = int(input())

dp = [0] * (1000001)
dp[1], dp[2] = 1, 2

for i in range(3, n+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 15746

print(dp[n])
'''

# 1932번. 정수 삼각형
'''
import sys 
n = int(input())
triangle = [list(map(int, input().split())) for _ in range(n)]

dp = [[0 for _ in range(len(triangle[i]))] for i in range(n)]

# 초기화
dp[0][0] = triangle[0][0]

for i in range(1, n):
    for j in range(len(triangle[i])):
        if j == 0:
            dp[i][j] = dp[i-1][j] + triangle[i][j]
        elif j == len(triangle[i]) - 1:
            dp[i][j] = dp[i-1][j-1] + triangle[i][j]
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]

print(max(dp[n-1]))
'''

# 방법 2
'''
import sys
n = int(input())

dp = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            dp[i][j] += dp[i-1][j]
        elif j == i:
            dp[i][j] += dp[i-1][j-1]
        else:
            dp[i][j] += max(dp[i-1][j-1], dp[i-1][j])

print(max(dp[n-1]))
'''


# 11053번 가장 긴 증가하는 부분 수열
'''
import sys
n = int(input())
A = list(map(int, sys.stdin.readline().split()))

# 모든 숫자가 수열이 될 수 있는 가능성을 가지고 있기 때문에 1로 초기화
dp = [1]*(n+1)

for i in range(n):
    # i 이전 값들과 비교
    for j in range(i):
        if A[j] < A[i]:
            dp[i] = max(dp[j]+1, dp[i])
print(max(dp))
'''