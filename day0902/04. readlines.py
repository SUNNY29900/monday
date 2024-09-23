#04. readlines.py
# 임포트 문장x, import file~~
# pathName='경로/파일.txt'
# 리턴변수 = open(파일, 모드w/r/a, 인코딩)
# 리턴변수.close()
# 임포트문장 없어요
# open(1,2,3)대체, with open(1,2) as ff: 

#파일읽기 read(), readline(), readlines()

fileName = 'C:/Mtest/kakao.txt'
with open(fileName,'r',encoding='UTF-8') as myfile:
     for data in myfile.readlines():
             print(data,end='')



print(fileName,'파일읽기성공했습니다')
print()
print()

