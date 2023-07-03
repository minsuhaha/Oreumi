# 전역변수와 지역변수
'''
global_var = 100
def my_func(global_var):
    local_var = 50
    global_var += 50
    # 함수안에서 외부 변수 값을 바꿀 수는 없다 -> 함수 내에서 global global_var 선언을 해줘야 함.
    print("전역 변수:", global_var)
    print("지역 변수:", local_var)
    return global_var

global_var = my_func(global_var)

print("전역 변수:", global_var)
# locar_var는 my_func 함수 내에서 정의한 변수이기에 함수 밖에서는 사용을 할 수 없다!
print("지역 변수:", locar_var)
'''

# 패킹
def get_person():
    return "하민수", 20, "haminsu5@gmail.com"
# 언패킹
name, age, email = get_person()

print(age)