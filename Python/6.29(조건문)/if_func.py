x = 10
# isinstance -> x의 타입이 str인지 확인
if isinstance(x, str):
    print('x는 정수입니다.')
else:
    print('문자형이 아닙니다')

# max, min
a = [1, 2, 3]
max = max(a)
min = min(a)
print(max, min)

# 대문자를 소문자로, 소문자를 대문자로
a = 'HELLO'
print(a.lower())
print(a.lower().upper())
