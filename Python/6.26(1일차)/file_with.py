with open('6.26(1일차)/a.txt', 'r') as f:
    content = f.read()
    print(content)
print(content)

# file.close() 원래 안해주면 메모리가 계속 쓰이고 있게 됨. 하지만 with open으로 파일을 열면 알아서 close도 됨