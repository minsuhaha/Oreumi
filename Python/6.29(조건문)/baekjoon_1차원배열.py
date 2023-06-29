# 알고리즘 4단계 1차원배열

'''
# 문제 10818번. 최소, 최대
n = int(input())
nums = map(int, input().split())
print(min(nums), max(nums))
'''

# 문제 10811번 바구니 뒤집기
'''
n, m = map(int, input().split())
nums = [i for i in range(1, n+1)]

for i in range(m):
    i, j = map(int, input().split())
    temp = nums[i-1:j] # <- 임의의 변수에 먼저 담아주고 reverse()를 써줘야 뒤집기 효과가 발생
    temp.reverse() # <- 이 줄 이후에 reverse 효과가 나타남
    nums[i-1:j] = temp

print(*nums)
'''

# 10798번. 세로읽기
'''
words = [input() for _ in range(5)]
max = len(words[0])
res = ''
for i in range(1, 5):
    if max < len(words[i]):
        max = len(words[i])
for i in range(5):
    if len(words[i]) < max:
        words[i] += ' '*(max-len(words[i]))
for i in range(max):
    for j in range(5):
        res += words[j][i]
res = res.replace(' ','') # <- replace 함수도 변수안에 담아서 사용해야 된다
print(res)
''' 
