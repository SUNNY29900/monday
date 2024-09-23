# 05ospath.py

# 임포트 문장x, import file~~
# pathName='경로/파일.txt'
# 리턴변수 = open(파일, 모드w/r/a, 인코딩)
# 리턴변수.close()
# 임포트문장 없어요
# open(1,2,3)대체, with open(1,2) as ff: 

#파일읽기 read(), readline(), readlines()

import sys
import os.path

file='C:/Mtest/kakao.txt'
save_path=os.path.abspath('C:/Mtest/my.txt')
try:
    if not os.path.exists(save_path):
       print(save_path, '대상 파일이 존재하지 않습니다')
       sys.exit()
    else:
       pass   
except Exception as EX:
     print('에러이유 확인', EX)

