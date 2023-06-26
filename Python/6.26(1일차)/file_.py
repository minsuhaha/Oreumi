# 경로 저장하기
file_path = "6.26(1일차)/title.txt"
# 파일 열기 (read 형태)
file = open(file_path, 'r')
content = file.read()
print(content)
file.close()

# 파일 만들고 쓰기 (write 형태)
file_path = "6.26(1일차)/context.txt"
file = open(file_path, 'w')
file.write("earse")
file.close()


# 파일 만들고 쓰기 (add 추가되는 형태)
file_path = "6.26(1일차)/context.txt"
file = open(file_path, 'a')
file.write(" not earse")
file.close()
