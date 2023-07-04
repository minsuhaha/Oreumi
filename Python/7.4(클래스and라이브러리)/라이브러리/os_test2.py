import glob
import os

# 현재 경로
current_path = os.path.abspath(__file__)
print(current_path)

# Downloads에 있는 전체 pdf 파일을 말함
pdf_files = glob.glob('/Users/haminsu/Downloads/*.pdf')

for pdf_file in pdf_files:
    print(pdf_file)