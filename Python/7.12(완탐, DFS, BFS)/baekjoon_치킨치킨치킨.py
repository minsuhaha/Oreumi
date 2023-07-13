import sys
from itertools import combinations

n, m = map(int,input().split())
chicken = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# ---------- 입력 부분 -------------

total_sum = 0
# i, j, z 는 chicken의 인덱스 값으로 생각
for i, j, z in combinations(range(m), 3):
    max_sum = 0
    for k in range(n):
        # 한사람씩 해당 치킨조합의 최대 선호도값 넣어주기
        max_sum += max(chicken[k][i], chicken[k][j], chicken[k][z])
    # 이전 total값과 다시 들어온 max_sum 값과 비교해서 더 큰 거 집어넣기
    total_sum = max(total_sum, max_sum)
print(total_sum)