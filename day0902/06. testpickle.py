# 06. testpickle.py

# open(파일명, 모드 wb/rb, 인코딩)
# dump쓰기/ load 읽기
# 피클로 파일처리 import

import pickle
import time
fileName='C:\Mtest/movie.pck1'
mybest={'슈퍼 super':9.72, '아이iron':7.45, '손흥민':5.3}

#일반파일처리 file.write('슈퍼 superman')    #피클은 다른 파일에서 못쓰도록 보호.
pickle. dump(mybest, open(fileName,'wb'))
print(fileName, '피클읽기 성공했습니다')
print('.'*60)
print()

time.sleep(1)
data=pickle.load(open(fileName,'rb'))
print(data)
