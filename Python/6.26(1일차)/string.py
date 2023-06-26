# 문자열 더해주기
str1, str2 = "hello", "world!"
print(str1+" "+str2)

# 문자 곱해주기 -> 반복
str1 = "오르미 강의 너무 재밌다!" * 10
print(str1)

# 문자열 인덱싱
str1 = "여기서 a는 몇번째 일까요?"
print(str1[4])

# 문자열 슬라이싱
str1 = "여기서 apple은 어디서부터 어디까지 일까요?"
print(str1[4:9])
print(str1[9:])
print(str1[:4])

# 문자열 전체길이 (전체 단어개수) -> 공백, 마침표등도 다 들어감
print(len(str1))