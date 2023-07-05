# Regular Expression (정규표현식)
import re

# pattern = r'apple'
# string = 'I have an apple and an orange.'

# result = re.search(pattern, string)
# print(result)

pattern = r'a[bcd]*d'
string = "ad, abcd, abbfd, acd"
result = re.findall(pattern, string)
print(result)