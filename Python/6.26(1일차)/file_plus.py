# r은 파일이 없으면 오류가 남.
# r과 r+는 차이가 없어야 됨.
file = open("6.26(1일차)/title2.txt" , 'r+')
context = file.read()
print(context)
file.close()


# w와 a는 따로 파일이 없어도 만들어줌
# w와 w+ 차이가 없음
file = open("6.26(1일차)/title3.txt" , 'w+')
file.write("w+로 추가해보기")
file.close()

# a와 a+ 도 차이가 없음
file = open("6.26(1일차)/content2.txt" , 'a+')
file.write("content")
file.close()

file = open("6.26(1일차)/context3.txt" , 'a')
file.write("content")
file.close()

