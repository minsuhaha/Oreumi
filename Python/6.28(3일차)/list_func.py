# append와 remove

'''
# for문으로 빈 배열에 append 하기
a = []
for i in range(1, 6):
    a.append(i)

# remove(지우고싶은원소) -> 배열에서 삭제해줌
a.remove(3)

# pop은 안에 인덱스를 넣고 지울 수 있음
a.pop(3)
'''

# sort와 슬라이싱

'''
a = [5, 3, 2, 4, 6, 1]
a.sort()
print(a)

a = [1, 2, 3, 4, 5, 6]
print(a[3:5])
'''

# list comprehension
'''
a = [i for i in range(1,6)]
print(a)
'''

# 배열 합치기 (확장) - extend
'''
a = [1, 2, 3]
b = [4, 5, 6]
a.extend(b)
print(a)

# +로도 합칠 수 있다.
a = a+b
print(a)

a = a * 3
print(a)
'''

# insert
a = [1,2,3]
b = [4,5,6]
a.insert(1,4)
print(a)

# pop(지우고싶은인덱스)
a = [1,2,3]
b = [4,5,6]
b.pop(2)
print(b)

# index(해당수) -> 해당 수의 인덱스 출력
print(a.index(2))

# len (길이)
print(len(a))

# count (해당원소) 가 몇개가 있는지
print(a.count(2))

# reverse -> 거꾸로
a.reverse()
print(a)


