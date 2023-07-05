# 예외처리
num1 = 10
num2 = 0

# ZeroDivisionError
# try:
#     result = num1 / num2
# # except ZeroDivisionError:
# #     print('0으로 나누시면 안돼요!')
# # as e 로 에러메세지 확인하기
# except Exception as e: 
#     print(str(e))

# finally:
#     print('에러가 나든말든 실행!')

# FileNotFoundError

# IndexError
# 

# TypeError
# try:
#     a = input()
#     result = a + 10
# except TypeError as e:
#     print(str(e))

# ValueError
# try:
#     a='a10'
#     int(a)
# except ValueError as e:
#     print(str(e))

# KeyError
try:
    mydict = {'key1':1, 'key2':2}
    print(mydict['key4'])
except KeyError as e:
    print(e)

# AttributeError
# KeyboardInterreupt
