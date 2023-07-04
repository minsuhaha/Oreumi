import os
folder_path = '/Users/haminsu/Documents/data-center'

if not os.path.exists(folder_path):
    # 폴더 생성
    os.makedirs(folder_path)
    print('f폴더 "{folder_path}"가 존재하지 않습니다.')
else:
    print('f폴더 "{folder_path}"가 존재합니다.')