file = open("6.26(1일차)/byte.txt", "rb")
context = file.read()
print(context)
file.close()

file = open("6.26(1일차)/byte.txt",  "wb")
file.write(b"hello")
file.close()