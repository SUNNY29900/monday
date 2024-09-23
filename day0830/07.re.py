#06re.py

import re

msg= 'mybest blue myjava my cherry blue mypython my '
x=re.findall( 'my' , msg )
y=re.findall( 'blue' , msg )
z=re.findall( 'red' , msg )
print(x)
print(y)
print(z)    #없으면 에러 대신  []  이런 형태로
print()

#msg 변수에 새로운 내용 원래내용 덮어씌우는 재할당
msg= 'my best %#@& 245 오렌지 수박 cherry as tea'

result1=re. findall('[\w]', msg)
result2=re. findall('[\w]', msg)
result3=re. findall('[a-zA-Z0-9]', msg)
print(result1)
print(result2)
print(result3)


print()
