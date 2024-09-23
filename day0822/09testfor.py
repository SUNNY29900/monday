# 09testfor.py

# 문자열,list,tuple,set,dict
# 반복데이터 사용
'''
for 변수대표k in range(10) :
    10회처리 0~9까지 10회처리 

for 변수대표k in range(1,10) :
    9회처리 1~9까지 9회처리 

for 변수대표k in range(1,10,1) :
    9회처리 1~9까지 9회처리 
    1씩증가일때 3번째 1생략

while 조건 :
  조건만족시 루프loop처리 
  무한루프처리일때 if제어문으로 break반복탈출  
'''

# for,while연습할때 사용 a,b,hap,tot
a,b=0,0
hap,tot=0,0

#첫번째 a, hap 1~5출력 누적
'''
 1  1
 2  3
 3  6
 4  10
 5  15
'''
a = a+1; hap=hap+a; print(a,hap)
a = a+1; hap=hap+a; print(a,hap)
a = a+1; hap=hap+a; print(a,hap)
a = a+1; hap=hap+a; print(a,hap)
a = a+1; hap=hap+a; print(a,hap)
print() 

#변수 재사용할때 

#for반복문, 대입연산
a,hap = 0,0 #점심식사후 변수초기화 
for a in range(5):
    a = a + 1
    hap = hap + a
    print(a, hap)






message = "Hello, World!"  # message 변수 정의
for k in range(5):
    print(k, message)





