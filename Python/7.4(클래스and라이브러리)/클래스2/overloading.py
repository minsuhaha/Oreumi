# over loading
def add(a,b):
    return a+b

def add(a,b,c):
    return a+b+c

print(add(2,3))

# python에서는 overload가 없다! -> 맨 아래에 있는 것만 불러옴
# 오버로드란 동일한 이름으로 서로 다른 매개변수를 가진 함수를 여러개 사용하는 것이다