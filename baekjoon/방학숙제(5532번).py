L = int(input()) # 총 방학 일수
A = int(input()) # 총 풀어야 되는 국어 페이지
B = int(input()) # 총 풀어야 되는 수학 페이지
C = int(input()) # 상근이 자식이 하루에 풀 수 있는 국어 페이지
D = int(input()) # 상근이 자식이 하루에 풀 수 있는 수학 페이지

while (A > 0 or B > 0):
    A -= C
    B -= D
    L -= 1
print(L)