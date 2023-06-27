# 백준 알고리즘별 분류 1단계 (입출력)

# 4번. AXB
'''
a, b = map(int, input().split())
print(a*b)

# 10번. 곱셈
num1 = int(input())
num2 = input()

a = num1*int(num2[2])
b = num1*int(num2[1])
c = num1*int(num2[0])

print(a)
print(b)
print(c)
print(num1*int(num2))

# 11번. 꼬마정민
a, b, c = map(int,input().split())
print(a+b+c)

# 12번. 고양이
print('\    /\\')
print(' )  ( ')')
print('(  /  )')
print(' \(__)|')
'''


# 백준 알고리즘별 분류 5단계 (문자열)

# 1번. 문자와 문자열
'''
s = input()
i = int(input())
print(s[i-1])


# 2번. 단어 길이 재기
word = input()
print(len(word))


#  3번. 문자열
n = int(input())
for i in range(n):
    word = input()
    print(f'{word[0]}{word[-1]}')


# 4번. 아스키 코드
print(ord(input()))


# 5번. 숫자의 합
n = int(input())
num = input()
total = 0
for i in range(n):
    total+=int(num[i])
print(total)
'''