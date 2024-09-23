#04testor.py

#변수선언 및 초기화
a, b, c = 7, 2, 4
x,y,z=False,False,False            #0초기화보다는 false권장

#관계연산 = 비교연산 > < >= <= == !=
#논리연산 and or not is in
x=((a >= b) and (b >= c))     #크거나 같으면
y=((a >= b) or (b >= c))  
z=(a != b)   

print('논리연산 and or test')
print(x)        #False
print(y)        #True
print(z)        #True

print()


