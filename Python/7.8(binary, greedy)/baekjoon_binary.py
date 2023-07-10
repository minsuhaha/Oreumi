# 수 찾기 1920번
'''
n = int(input())
A = sorted(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

def binary_search(start, end, B, A):
    while start <= end:
        mid = (start + end) // 2
        if A[mid] == B:
            return 1
        elif A[mid] < B:
            start = mid + 1
        else:
            end = mid - 1
    return 0

for b in B:
    result = binary_search(0, len(A)-1, b, A)
    print(result)
'''

# 랜선 자르기 1654번
# 점심먹고 손으로 다시 풀어보기, 디버깅 해보자
# -> 정렬해보고 초반 중간 지점을 찾아볼까?
'''
import sys
k, n = map(int, input().split())
length = [int(sys.stdin.readline()) for _ in range(k)]

def binary_search(start, end):
    while start <= end:
        cnt = 0
        mid = (start + end) // 2
        # 총 만들 수 있는 랜선의 개수
        for i in range(k):
            cnt += (length[i] // mid)
        if cnt < n:
            end = mid - 1
        elif cnt >= n:
            start = mid + 1
    # 최대길이를 구해야 하니깐 end 값 반환
    return end

result = binary_search(1, max(length))
print(result)
'''
'''
1.  아래 문제는 그리디 알고리즘과 이분탐색중에 어떤 알고리즘을 사용하는게 좋을까요? 그리고 그 이유는 무엇인가요?

문제:
현빈이는 자신의 코딩 강의를 영상으로 만들어 판매하려고 한다. 
영상에는 총 N개의 강의가 들어가는데, 영상안에 강의의 순서가 바뀌면 안 된다. 
즉, i번 강의와 j번 강의를 같은 영상파일에 녹화하려면 i부터 j까지의 모든 강의 또한 같은 영상파일에 녹화를 해야한다.
현빈이는 얼마나 강의가 인기 있을지를 몰라서 영상의 개수를 가급적 줄이려고 한다. 
오랜 고민 끝에 현빈이는 영상의 크기가 같은 M개의 영상파일에 저장을 하려고 한다.
현빈이의 각 강의의 길이가 분 단위(자연수)로 주어진다. 이때, 가능한 영상의 크기 중 최소를 구하는 프로그램을 작성하시오.

입력 예시:
9 3
1 2 3 4 5 / 6 7 / 8 9

출력예시:
17
'''

# n -> 강의 수, m -> 영상파일

def video_size(N, M, lecture_lengths):
    start = 1  
    end = sum(lecture_lengths)  

    while start <= end:
        mid = (start + end) // 2  
        count = 1  
        size = 0  

        for length in lecture_lengths:
            if size + length <= mid:
                size += length  
            else:
                count += 1  
                size = length  
        if count <= M:
            end = mid - 1
    
        else:
            start = mid + 1

    return start

N, M = map(int, input().split())
lecture_lengths = list(map(int, input().split()))

video_size = video_size(N, M, lecture_lengths)
print(video_size)
