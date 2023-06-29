# 1번째 방법
data = []
with open('Python/6.29(4일차)/file_1.txt', 'r') as f:
    # content = f.read()
    for line in f.readlines():
       data.append(line.rstrip())
data.sort()
print("전체 정렬: ", data)
print("전체 개수: ", len(data))
print("중복을 제거하고 남은 개수: ", len(set(data)))


# 2번째 방법
with open('Python/6.29(4일차)/file_1.txt', 'r') as f:
    content = f.read()
# 1. 전채정렬
lines = content.split('\n')
sorted_lines = sorted(lines, key=lambda x: x[0])
sorted_text = '\n'.join(sorted_lines)
print(sorted_text)

# 2. 전체개수
lines = content.split('\n')
print(len(lines))

# 3. 중복을 제거하고 남은 개수
lines = content.split('\n')
new_lines = list(set(lines))
print(len(new_lines))


