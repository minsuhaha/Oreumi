# dict 자유자재로 만지기
'''
gangsa = [{"이름":"김도언", "나이":20, "직업":"강사", "일일퀴즈성적":[10,20,20]},
{"이름":"이예원", "나이":20, "직업":"강사", "일일퀴즈성적":[9,19,19]}]

gangsa_add_info = {"회사":"이스트소프트", "강의기수":"2기"}

for i in range(len(gangsa)):
    gangsa[i].update(gangsa_add_info)
print(gangsa)
'''

'''
# 값 변경
a['나이'] += 6

# 새로운 키, value값 추가
a['주소'] = "서울대입구역"
print(a)

# 값 제거
del a['일일퀴즈성적']
print(a)

# key:value 개수
print(len(a))
'''

'''
# dict items 가져오기
for key, value in a.items():
    print(key,value)

# dict key값만 가져오기
for key in a.keys():
    print(key)

# dict value값만 가져오기
lst = []
for value in a.values():
    lst.append(value)
print(lst)
'''

# 두가지 이상의 items를 dict에 한번에 추가하기 위해서는 update 사용!
# a.update(c)
# print(a)