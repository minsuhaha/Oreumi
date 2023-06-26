# format 사용하기 문자열뒤에 .format
print("{} + {} = {} 입니다".format(1,2,3))

# {}안에 인덱스 숫자를 넣어줄수도 있음
print("내가 제일 좋아하는 과일은 {1}, 두번째는 {0}".format("수박","사과"))

a,b = 2,3
print("{} + {} = {} 입니다".format(a,b,a+b))

# f를 이용한 출력방법 (f-string)
a,b = 2,3
print(f"{a} + {b} = {a+b} 입니다")

# a에 저장된 값 메모리 주소 확인해보기 -> id(a)
print(id(a))