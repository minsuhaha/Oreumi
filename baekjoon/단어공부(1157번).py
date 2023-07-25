# 전부 대문자로 바꿔버림
words = input().upper()

# 중복 문자 제거
set_words = list(set(words))

lst = []
for word in set_words:
    lst.append(words.count(word))

# max 값이 두개 이상 일 경우
if lst.count(max(lst)) >= 2:
    print('?')
else:
    print(set_words[lst.index(max(lst))])