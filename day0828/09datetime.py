#09jumin.py



import datetime
import time

#x= dateim.now()    #에러
# print(x)
y= datetime.datetime.now()   #정답
print(y)   #2024-08-28 11:19:22.624677
print(str(y))  #안전화  2024추출
print(str(y)[0:4])   #2024
z=str(y)
print(z[0:4]) #2024-2001=나이계산산
print()


dt= datetime.datetime.now()  
print(dt.strftime('%Y년-m월-%d일'))
print(dt.strftime('%H시-M분-%S초'))

mytime=time.localtime()
print(mytime)
print(mytime.tm_year)   #2024년도 나이계산

