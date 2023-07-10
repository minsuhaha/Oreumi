# 그리디 알고리즘
# 1. 당장 현재에서 최선의 선택을 함
# 2. 모든 경우의 수 따지지 x

# 동전 0 11047번
'''
n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
cnt = 0

for i in reversed(range(n)):
    cnt += k // coins[i]
    k = k % coins[i]
print(cnt)
'''

# ATM 11399번
# 1번째 방법
'''
import sys
n = int(sys.stdin.readline())
times = list(map(int, sys.stdin.readline().split()))
times.sort()
total = 0
total_time = 0
for time in times:
    total += time
    total_time += total
print(total_time)

# 2번째 방법
n = int(sys.stdin.readline())
times = list(map(int, sys.stdin.readline().split()))
times.sort()
total_time = 0
for i in range(1, n+1):
    total_time += sum(times[0:i])
print(total_time)
'''

# 회의실 배정 1931번
'''
n = int(input())
times = [list(map(int, input().split())) for _ in range(n)]

# 끝나는 시점을 기준으로 먼저 정렬 후 끝나는 시점이 같은 경우 시작시간이 빠른 순으로 정렬
times.sort(lambda x : (x[1], x[0]))

cnt = 0
end, last_end = 0, 0

for time in times:
    end = time[1]
    if last_end <= time[0]:
        cnt += 1
        last_end = end
print(cnt)
'''

# 입국심사
'''
n, m = map(int, input().split())
times = [int(input()) for _ in range(n)]


def binary(n, times):
    # start = 1로 최소 수 설정
    start = 1 
    # end 지점은 m명의 친구들이 심사를 받는데 걸리는 최대시간을 잡기 (times에서 가장 긴 시간에만 심사를 받는다고 생각)
    end = max(times)*m 
    while start <= end:
        # 루프를 빠져나가는 조건이 아닐때 반복해서 mid 값 구해주기
        mid = (start+end) // 2
        # cnt 변수 초기화
        cnt = 0

        # 현재 임의의 mid 시간안에 심사를 받을 수 있는 사람의 수
        for i in range(n):
            cnt += (mid // times[i])

        # cnt 수가 같다고 하더라도 최소 걸리는 시간을 구하기 위해 if cnt > m 가 아닌 if cnt >= m으로 설정
        if cnt >= m:
            end = mid - 1
        # cnt 가 m보다 작을 때 현재 mid값 보다 작은 범위는 신경 안써도 되기 때문에 start 지점 범위 변경해주기
        elif cnt < m:
            start = mid + 1

    # 최솟값을 구할 때는 start / 최대값을 구할 땐 end 반환
    return start
 
result = binary(n, times)
print(result)
'''
