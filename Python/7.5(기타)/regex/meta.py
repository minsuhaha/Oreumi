import re

# patterns = r'b.t' # 한글자
# string = 'bat, b@t, bit, but, baat, beet'

# pattern = r'ab+c' # a와 c는 한개로 고정 사이 b는 1개이상 가능! abbc, abbbc, abbbbc등
# string = 'ac, abc, abbc, abbbc, abdc'

# pattern = r'ab*c'  # *-> 0개이상 / + -> 1개이상
# string = 'ac, abc, abbc, abbbc, abdc'

# pattern = r'(ab)+c'  # *-> 0개이상 / + -> 1개이상
# string = 'abc, ababc, abababc, ab, aabb'

# pattern = r'[aeiou]' # []안에 있는 어떠한 문자와도 매칭을 시켜준다. r'[a-z]' , r'[A-Z]'
# pattern2 = r'[0-9]' # [0-9] 0부터 9까지의 숫자를 하나씩 전부 매칭

# string = 'apple, orange, banana'
# string2 = '123456789'

# pattern = r'\d'   # 모든 숫자들을 한개씩 매칭   / 1, 0 ,5
# string = 'I have 10 apples and 5 bananas'

# pattern = r'\d+'   # 연속된 숫자를 찾고 싶을 때   / 10 ,5
# string = 'I have 10 apples and 5 bananas'

# pattern = r'\w'   # 특수문자를 제외한 문자 또는 숫자를 _ 전부 다 찾는거
# string = 'I have 10 apples and 5 bananas!!!'

# pattern = r'\w+'   # 특수문자를 제외한 문자단어 단위로 찾기
# string = 'I have 10 apples and 5 bananas!!!'

# pattern = r'^Hello'  # ^ -> 시작점 확인
# string = 'Hello, World! Hello, Python!'

# pattern = r'thon!$'  # $ -> 뒷부분 확인
# string = 'Hello, World! Hello, Python!'

# pattern = r'a{1,3}' # a{3} -> a가 3만큼 반복된것들 / a{1,3} a가 1~3개인 것들
# string = 'ab, abc, aabc, aaabc'

# pattern = r'a|b' # a 또는 b 전부 다 [ab]와 똑같다
# string = 'ab, abc, aabc, aaabc'
 
# pattern = r'(ab)+' #ab를 하나의 단어로 생각하고 찾음
# string = 'ab, abab, ababc'

# result = re.match(pattern, string)
# print(result.group())

# result = re.findall(pattern, string)
# print(result)

string = "문장 속에는 다양한 URL이 있습니다. https://www.example.com/, http://subdomain.example.co.kr/, www.google.com, ftp://fileserver.example.org, 이렇게 다양한 형식의 URL이 있습니다."
pattern = r"[a-z0-9.:/-]+[0-9a-z.]+[a-z./]+"

# sub 바꿔치기
result = re.sub(pattern,'',string)
print(result)
