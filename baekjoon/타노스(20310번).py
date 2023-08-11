s = input()

new_s = s.replace('1','',s.count('1')//2)

# 뒤집기
new_s = new_s[::-1]

new_s = new_s.replace('0', '', s.count('0')//2)

# 다시 뒤집기
new_s = new_s[::-1]

print(new_s)