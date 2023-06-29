# 소수 판별 --> 자기자신과 1 외에 나눠지는 숫자가 없으면 소수
n = int(input())

is_prime = True
for i in range(2, int((int(n**0.5)))+1):
    if n%i == 0:
        print("소수가 아님")
        is_prime = False
        break
if is_prime:
    print("소수이다")