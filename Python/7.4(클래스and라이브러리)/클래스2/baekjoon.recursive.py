# 백준 재귀문제

# 27433번. 팩토리얼 2
'''
n = int(input())
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(n))
'''

# 10870번. 피보나치 수 5
n = int(input())

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(n))
