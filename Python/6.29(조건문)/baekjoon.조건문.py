# 알고리즘별 2단계(반복문) 

# 1330번. 두 수 비교하기
'''
a, b = map(int, input().split())
if a > b:
    print('>')
elif a < b:
    print('<')
else:
    print('==')
'''

# 9498번. 시험 성적
'''
n = int(input())
if n >= 90:
    print("A")
elif n >= 80:
    print("B")
elif n >= 70:
    print("C")
elif n >= 60:
    print("D")
else:
    print("F")
'''

# 2753번. 윤년
'''
n = int(input())
if (n % 4) == 0 and ((n%100) != 0 or (n%400) == 0):
    print(1)
else:
    print(0)
'''
# 14681번. 사분면 고르기
'''
x = int(input())
y = int(input())

if x>0 and y>0:
    print(1)
elif x<0 and y>0:
    print(2)
elif x<0 and y<0:
    print(3)
else:
    print(4)
'''

# 2525번 오븐 시계
'''
a, b = map(int, input().split())
c = int(input())

a += (b+c) // 60
b = (b+c) % 60

if a > 23:
    a = a - 24
print(f'{a} {b}')
'''

# 2884번 알람 시계
import sys
H, M = map(int, sys.stdin.readline().split())

if M < 45:
    if H == 0:
        H = 23
        M += 15 # <-- 45분만 빼주면 되는데 1시간을 빼줬기 때문에 M+=15 해주기
    else:
        H -= 1
        M += 15
else:
    M -= 45
print(H,M)





# 2480번. 주사위 세개
'''
a, b, c = map(int, input().split())

if a == b == c:
    print(10000 + a*1000)
elif a==b or b==c:
    print(1000+b*100)
elif a==c:
    print(1000+a*100)
else:
    print(max(a,b,c)*100)
'''