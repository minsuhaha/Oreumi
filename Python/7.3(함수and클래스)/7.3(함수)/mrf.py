# map(함수, 리스트or튜플)
'''
numbers = [1,2,3,4,5,6]
plus = list(map(lambda x:x+1, numbers))
print(plus)
'''

# reduce 누적으로 더해 줄 수 있음 앞에 결과 계산값이 x에 들어감
'''
from functools import reduce
numbers = [1, 2, 3, 4, 5]
sum = reduce(lambda x, y : x+y, numbers)
print(sum)
'''

# filter
'''
numbers = [1,2,3,4,5,6]
even = list(filter(lambda x:x%2 != 0, numbers))
print(even)
'''

# sum
# print(sum(numbers))


# from functools import reduce
# numbers = ['letter', 'bigger']
# upper_num = list(map(lambda x:x.upper(), numbers))
# print(upper_num)