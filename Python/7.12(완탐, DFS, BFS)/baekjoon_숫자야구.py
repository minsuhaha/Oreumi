from itertools import permutations
n = int(input())

numbers = list(permutations(range(1,10), 3))

# numbers 안의 값을 바꿔주기 위해서는 튜플 -> 리스트로 변경해줘야 함.
numbers = list(map(lambda x:list(x), numbers))

for _ in range(n):
    num, s, b = map(int, input().split())
    num = list(str(num))
    
    for i in range(len(numbers)):
        s_count = 0
        b_count = 0

        for j in range(len(num)):
            if int(num[j]) == numbers[i][j]:
                s_count += 1
            elif int(num[j]) in numbers[i]:
                b_count += 1
        
        if s != s_count or b != b_count:
            numbers[i][0] = 0
cnt = 0
for number in numbers:
    if number[0] != 0:
        cnt+=1
print(cnt)
         
         