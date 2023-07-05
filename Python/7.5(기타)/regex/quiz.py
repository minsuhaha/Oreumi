# 전화번호 찾기
import re
pattern = r'\d{2,3}-\d{3,4}-\d{4}'
phone = "내 전화번호는 !-010-4444-1234-! 이야 125!22%13 지역번호가 155542-10-1"
phonenumber = re.findall(pattern, phone)
print(phonenumber)

# 이메일 주소 추출
import re

pattern = r'[\w]+@[a-z]+.[a-z]+'
string = "안녕하세요. 이메일 주소는 abc@example.com입니다. asdasdsad 다른 이메일은 def@example.com이고, xyz@example.com도 있습니다."
email = re.findall(pattern, string)
print(email) 

# url 추출
pattern = r'[a-z:/]+.[\w.]+.[a-z/]+'
string = "문장 속에는 다양한 URL이 있습니다. https://www.example.com/, http://subdomain.example.co.kr/, www.google.com, ftp://fileserver.example.org, 이렇게 다양한 형식의 URL이 있습니다."
email = re.findall(pattern, string)
print(email) 