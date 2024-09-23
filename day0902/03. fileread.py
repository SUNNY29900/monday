# 3.fileread.py

# 임포트 문장x, import file~~
# pathName='경로/파일.txt'
# 리턴변수 = open(파일, 모드w/r/a, 인코딩)
# 리턴변수.close()
# 임포트문장 없어요
# open(1,2,3)대체, with open(1,2) as ff: 

import time
#파일읽기 처리   read()대신 readline()한라인씩 읽기
pathName = 'C:/Mtest/sample2.txt'
rfile = open(pathName, 'r', encoding='UTF-8')
#data=rfile.read()
data=rfile.readline()   #한줄씩 처리
print(data)
print('.'*50)
print(pathName,'파일읽기성공했습니다')
print()

time.sleep(1)
fileName = 'C:/Mtest/kakao.txt'
with open(fileName,'r',encoding='UTF-8') as myfile:
    #my = myfile.read()    #전체 읽어서 출력
     my = myfile.readlined()   #한줄씩 처리
     while my !='':
          print(my)
          my = myfile.readline()

print(fileName,'파일읽기성공했습니다')
print()
print()

