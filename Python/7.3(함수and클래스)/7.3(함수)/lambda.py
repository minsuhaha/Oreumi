# add = lambda a, b : a+b
# result = add(2,3)
# print(result)

'''
numbers = [1, 2, 3, 4, 5]
# map함수는 for 처럼 하나하나씩 돈다 라고 생각하자! map(함수, 적용리스트(튜플도가능))
# lambda 매개변수 : 매개변수에 대한 결과 값 : lambda x:x+1
squared = list(map(lambda x:x+1, numbers))
print(squared)
'''

student = [
    {'name' : '이민영', 'age' : 23},
    {'name' : '양승조', 'age' : 17},
    {'name' : '문기원', 'age' : 25},
]

student.sort(key = lambda x:x['age'])
print(student)


