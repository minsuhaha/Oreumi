'''
a, b = map(int, input().split())
# 최대공약수 구하기 함수
def gcd(a, b):
    while b!=0:
        a, b = b, a%b
    return a

# 최소공배수 구하기
print((a*b) // gcd(a,b))

# 최대공약수 구하기
print(gcd(a,b))
'''

n = int(input("소인수 분해할 숫자를 입력해주세요!"))
# 소인수분해
factors = []
while n % 2 == 0:
    factors.append(2)
    n //= 2 
    
i = 3
while i*i <= n:
    while n % i == 0:
        factors.append(i)
        n //= i
    i += 2 
if n > 1:
    factors.append(n)

print(factors)