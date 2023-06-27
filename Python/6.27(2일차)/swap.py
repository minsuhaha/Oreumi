# 배열의 위치 바꾸기

# 1번째 뒤집는 방법
# a = [1, 2, 3, 4 ,5]
# print(a[::-1])

# 2번째 방법
# a = [1, 2, 3, 4 ,5]
# a.reverse()
# print(a)

# 3번째 방법
# a = [1, 2, 3, 4 ,5]
# left = 0
# right = len(a) - 1
# while left < right:
#     a[left], a[right] = a[right], a[left]
#     left+=1
#     right-=1
# print(a)

# 이중 for 문 간단 예시
for i in range(3):
    for j in range(3):
        print(i,j)