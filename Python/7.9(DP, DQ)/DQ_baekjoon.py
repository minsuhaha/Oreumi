# 2630번 색종이 만들기
'''
import sys

N = int(input())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

result = [] # 첫번째 결과에는 하얀색 색종이를, 두번재 결과에는 파란색 색종이를 저장

# x좌표, y좌표, 전체길이 N을 매개변수로 넣어준다
def solution(row, col, N):
    color  = paper[row][col]
    for i in range(row, row+N):
        for j in range(col, col+N):
            # 현재의 color가 paper 안 사분면에서 어느 하나라도 다를 시
            if color != paper[i][j]:
                solution(row, col, N//2)
                solution(row, col+(N//2), N//2)
                solution(row+(N//2), col, (N//2))
                solution(row+(N//2), col+(N//2), N//2)
                return

    if color == 0:
        result.append(0)
    else:
        result.append(1)

solution(0, 0, N)
print(result.count(0))
print(result.count(1))
'''

# 1780번. 종이의 개수
import sys
n = int(input())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
result = []
def solution(row, col, N):
    color = paper[row][col]
    for i in range(row, row+N):
        for j in range(col, col+N):
            if color != paper[i][j]:
                # 반복해서 분할 하기 위해 9개의 분면으로 분할
                for k in range(3):
                    for l in range(3):
                        solution(row+(N//3)*k, col+(N//3)*l, N//3)
                return
    if color == -1:
        result.append(-1)
    elif color == 0:
        result.append(0)
    else:
        result.append(1)

solution(0, 0, n)

print(result.count(-1))
print(result.count(0))
print(result.count(1))


'''
import sys

# 1. 입력받기 
n = int(input())
paper = []
for i in range(n):
    paper.append(list(map(int,sys.stdin.readline().split())))

# 종이 종류 RESULT 
result = {-1:0, 0:0,1:0}

# 2. 종이의 종류(-1, 0, 1)와 다르면 분할 
def divided(row,col,n):
    curr = paper[row][col] # 종이의 시작 

    for i in range(row, row+n):
        for j in range(col, col+n):
            # 현재 종이 종류와 다르다면 
            if paper[i][j] != curr:
                # 종이 1/3로 분할 (ex. n == 9 , n = 9 -> 3 -> 1 )
                next = n//3
                # 종이를 같은 크기의 종이 9개로 자르므로 
                divided(row, col, next) # 1번째 block (0,0)
                divided(row, col+next, next) # 2번째 block (0,1)
                divided(row, col+(next*2), next) # 3번째 block (0,2)
                divided(row+next, col, next) # 4번째 block (1,0)
                divided(row+next, col+next, next) # 5번째 block (1,1)
                divided(row+next, col+(next*2), next) # 6번째 block (1,2)
                divided(row+(next*2), col, next) # 7번째 block (1,0)
                divided(row+(next*2), col+next, next) # 8번째 block (1,1)
                divided(row+(next*2), col+(next*2), next) # 9번째 block (1,2)
                return 

    # 3. 종이 종류에 따라 count 
    result[curr] +=1 
    return 

divided(0,0,n)

# 4. 결과 return 
for i in result.values():
    print(i)
'''