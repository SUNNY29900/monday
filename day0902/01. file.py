# 1.file.py

# 임포트 문장x, import file~~
# pathName='경로/파일.txt'
# 리턴변수 = open(파일, 모드w/r/a, 인코딩)
# 리턴변수.close()
# 임포트문장 없어요
# open(1,2,3)대체, with open(1,2) as ff: 

import time
pathName = 'C:/Mtest/sample.txt'
wfile = open(pathName, 'a', encoding='UTF-8')
name = input('이름입력>>> ')
age = input('나이입력>>> ')
juso = input('주소입력>>> ')

wfile.write(name + '\n')
wfile.write(age  + '\n')
wfile.write(juso + '\n')
wfile.close() #추천권장

time.sleep(0.5)
print(pathName,'파일저장성공했습니다')
print()


print('-' * 70)
time.sleep(1)
fileName = 'C:/Mtest/kakao.txt'
with open(fileName,'a',encoding='UTF-8') as myfile:
    name = input('이름입력>>> ')
    age = input('나이입력>>> ')
    juso = input('주소입력>>> ')

    myfile.write(name + '\n')
    myfile.write(age  + '\n')
    myfile.write(juso + '\n')
    
#생략가능 myfile.close()
time.sleep(0.5)
print(fileName,'파일저장성공했습니다')
print()
