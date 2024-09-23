# 2.file.py

# 임포트 문장x, import file~~
# pathName='경로/파일.txt'
# 리턴변수 = open(파일, 모드w/r/a, 인코딩)
# 리턴변수.close()
# 임포트문장 없어요
# open(1,2,3)대체, with open(1,2) as ff: 

import time
#파일읽기 처리
pathName = 'C:/Mtest/sample2.txt'
rfile = open(pathName, 'r', encoding='UTF-8')
data=rfile.read()
#주석 data=rfile.readline()
print(data)
print('.'*50)
rfile.close() 
time.sleep(0.5)
print(pathName,'파일읽기성공했습니다')
print()

time.sleep(1)
fileName = 'C:/Mtest/kakao.txt'
with open(fileName,'r',encoding='UTF-8') as myfile:
     my = myfile.read()
     print(my)

print(fileName,'파일읽기성공했습니다')
print()
print()

