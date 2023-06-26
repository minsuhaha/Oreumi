# 한줄 주석
print("hello, oreumi!")
print("nice to meet you")


''' 여러줄 주석 처리
1
2
3줄
'''

def add(num1, num2, num3):
    '''
    함수에 대해서 설명을 넣기 위한 주석
    add 함수입니다.
        Args:
            a 'str' : a value
            b 'int' : b value
            c 'str' : c value
        Returns:
            None            
    '''
    return num1 + num2 + num3
print(add())