# 1. 이분탐색 알고리즘을 사용하기 위해서는 정렬이 되어 있어야 한다.
# 2. start, mid, end 값을 기준으로 탐색 시작
# 3. 맨 처음의 인덱스가 start, 맨 마지막 인덱스가 end
# 4. 정답과 mid값이 같을 때 까지 (start + end) // 2 = mid 반복 실행
# 5. mid 값 보다 정답 값이 크면 end = mid 로, mid 값이 정답 값 보다 작으면 start = mid 로 바꿔주고 탐색 진행  

def binary_search(start, end, target, array):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

array = [1, 2, 3, 4, 5]
target = 4

result = binary_search(0, len(array)-1, target, array)
print(result)
