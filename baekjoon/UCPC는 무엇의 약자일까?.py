content = input()
# 공백을 기준으로 배열로 만들어주기
words  = content.split(' ')

find_word = 'UCPC'
idx = 0
for word in words:
    if find_word[idx] in word:
        idx += 1
    if idx == 4:
        print('I love UCPC')
        break
        
if idx != 4:
    print('I hate UCPC')