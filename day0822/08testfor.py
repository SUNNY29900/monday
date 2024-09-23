#08testfor.py


#문자열, 리스트출력, tuple, set, dict
#반복데이터 사용

'''
for 변수대표k in range(10) : 
    10회처리 0~9 10회처리
for 변수대표k in range(1, 10) : 
    9회처리 1~9 9회처리
for 변수대표k in range(1, 10, 1) : 
    9회처리 1~9 9회처리
    1씩 증가할때 3번째 1생략

while 조건
    조건만족시 루프loop처리
    무한루프처리일때 if제어문으로  break반복 탈출

'''

#for, while 연습할때 사용 a,b,hap,tot
a,b=0,0
hap,tot=0,0

message='hello 길동!!!'
print(message) 
print(message) 
print(message) 
print(message) 
print(message) 
print() 

for k in range(5) : 
    print(k,message)
    #0부터 시작~4 =5회처리
    #10진수 0~9    2진수 0,1   8진수 0~7    16진수 0~9abcdef...
print()

