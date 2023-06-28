# 1546번 평균
'''
import sys
n = int(sys.stdin.readline())
scores = list(map(int, input().split()))
total = 0
max_score = max(scores)
for score in scores:
    total += ((score/max_score)*100)
print(total/n)
'''

# 4150번 피보나치 수
'''
import sys
n = int(sys.stdin.readline())
curr, next = 0, 1
for i in range(2, n+1):
    curr, next = next, curr + next
print(next)
'''

# 2741번 N찍기
'''
import sys
n = int(sys.stdin.readline())
for i in range(1, n+1):
    print(i)
'''

# 2742번 기찍 N
'''
import sys
n = int(sys.stdin.readline())
for i in range(n, 0, -1):
    print(i)
'''

# 1924번 2007년
'''
import sys
x, y = map(int, sys.stdin.readline().split())
# 1년 총 일자
cnt = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
total_day = y
if x > 1:
    for i in range(x-1):
        total_day += cnt[i]

print(day[total_day%7])
'''     


