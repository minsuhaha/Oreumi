# 알고리즘별 3단계(반복문) 
'''
# 문제 1. 구구단
n = int(input())
for i in range(1,10):
    print(f'{n} * {i} = {n*i}')


# 문제 2. A+B -3
n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    print(a+b)

# lst = [list(map(int, input().split())) for _ in range(n)]
# for i in range(n):
#     print(sum(lst[i]))


# 문제 3. 합
n = int(input())
total = 0
for i in range(1, n+1):
    total += i
print(total)


# 문제 4. 영수증
total_price = int(input())
n = int(input())
total = 0
for _ in range(n):
    price, cnt = map(int, input().split())
    total += (price*cnt)
print('Yes') if total_price == total else print('No')


# 문제 5. 코딩은 체육과목 입니다.
n = int(input())
cnt = n//4
result = 'long '*cnt
print(f'{result}int')


# 문제 6. 빠른 A+B
# Python을 사용하고 있다면, input 대신 sys.stdin.readline을 사용할 수 있다. 
# 단, 이때는 맨 끝의 개행문자까지 같이 입력받기 때문에 문자열을 저장하고 싶을 경우 .rstrip()을 추가로 해 주는 것이 좋다.
import sys
input = sys.stdin.readline
t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    print(a+b)


# 문제 7. A+B-7
import sys
input = sys.stdin.readline
t = int(input())
for i in range(1, t+1):
    a, b = map(int, input().split())
    print(f'Case #{i}: {a+b}')


# 문제 8. A+B - 8
import sys
imput = sys.stdin.readline
t = int(input())
for i in range(1, t+1):
    a, b = map(int, input().split())
    print(f'Case #{i}: {a} + {b} = {a+b}')
'''


