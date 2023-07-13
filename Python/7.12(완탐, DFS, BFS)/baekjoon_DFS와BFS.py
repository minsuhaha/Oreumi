from collections import deque
n, m, v = map(int, input().split())

# 연결 관계를 나타낼 graph 초기화
graph = [[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    # 간선으로 이어져 있는 노드들을 graph 상에 표시
    graph[a][b] = 1
    graph[b][a] = 1

# 방문표시를 하기 위한 visited 배열 생성
visited1 = [0] * (n+1)
visited2 = [0] * (n+1)

# 깊이우선탐색
def dfs(v):
    # 시작지점 방문처리
    visited1[v] = 1 
    print(v, end = ' ')
    for i in range(1, n+1):
        if graph[v][i] == 1 and visited1[i] == 0:
            # 그래프 상에는 연결되어진 부분인데 아직 방문처리가 되지 않았다면 방문처리
            visited1[i] = 1
            # 깊이우선 탐색이기에 방문처리가 되어진 것이 있다면 바로 재귀함수 실행
            dfs(i)

dfs(v)

# 너비우선탐색
def bfs(v):
    queue = deque([v])
    
    # queue 배열이 비어있지 않을 때까지 반복
    while queue:
        visited2[v] = 1
        # 가장 앞부분에 있는 값 꺼내기
        node = queue.popleft()
        print(node, end = ' ')

        for i in range(1, n+1):
            # graph에 해당 값이 연결되어 있고 아직 방문을 하지 않은
            if graph[node][i] == 1 and visited2[i] == 0:
                # 방문처리로 바꿔주기
                visited2[i] = 1
                # i씩 뒤로 줄줄이 해줘도 되는 이유는 queue에서는 popleft()를 통해 맨 앞에 있는 값만 꺼내기 때문에
                # 방금 방문처리한 값을 queue에 넣어주기
                queue.append(i)
print()
bfs(v)