message = b'\xbc\xd3\xd3\xcd'

# 가능한 모든 코덱을 확인
with open('7.7(Final)/codecs.txt', 'r') as f:
    codecs_list = f.read().replace('\n','').replace(',','').split()
print(codecs_list)

# for codec in codecs_list:
#     try:
#         print(message.decode(codec), codec)
#     except:
#         pass

