# HWpickle.py

# open(파일명, 모드 wb/rb, 인코딩)
# dump쓰기/ load 읽기
# 피클로 파일처리 import

import pickle
import time
import sys
import os.path

path='C:\Mtest/mydaily.txt'
while True:
    print()
num=int(input('1. 스케줄기록 2. 스케줄 읽기  9. 종료'))

if num ==1:  #피클. dump()
    file=open(path, 'wb')
    memo=inout("할일입력")
    pickle.dump(memo, file)
    file.close()
    print(path, '피클 저장기록처리 성공했습니다')  



elif  num==2:      #피클. load()
    file=open(path, 'rb')
    data=pickle.load(file)
    print(data)
    file.close()
    print(path, '피클 오픈읽기처리 성공했습니다')
elif  num==9:
    print('스케줄 피클처리 종료합니다')
    sys.exit()
else:
    print('작업번호 오류입니다')
print()
