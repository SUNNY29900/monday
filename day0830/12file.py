#12file.py


#리턴변수=open(파일, 모드 w/r/a, 인코딩)
#리턴변수.close()
#임포트문장 없어요

import time

pathNme='C:/Mtest/sample.txt'
wfile=open(pathNme, 'a', encoding='UTF=8')  #'a를 쓰면 덮어씌윅 /'wfile=open(pathNme, 'w', encoding='UTF=8')
name=input('이름입력>>>')
age=input('나이입력>>>')
juso=input('주소입력>>>')

wfile.write(name+'\n')
wfile.write(age+'\n')
wfile.write(juso+'\n')
wfile.close()   #추천권장

print('sample.txt파일저장 성공했습니다')
print()


#2
print('.'*70)
time.sleep(1)
pathNme2='C:/Mtest/sample2.txt'
with open(pathNme2, 'a', encoding='UTF-8') as myfile:
    name=input('이름입력>>>')
    age=input('나이입력>>>')
    juso=input('주소입력>>>')

    myfile.write(name+'\n')
    myfile.write(age+' \n')
    myfile.write(juso+'\n')

print('sample.txt파일저장 성공했습니다')
print()



