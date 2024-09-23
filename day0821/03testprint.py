#03testprint.py

#선언
a,b,ret=7,4,0
ret=a*b

#연산1
#print(변수, '문자', ~~), 나열식
print(a, '*', b, '=', ret)

#연산2
#print('%d, %d, %d' %(a,b,ret))
print('%d, %d, %d'% (a,b,ret))

#연산3
#print(f'{변수 및 값}')
print(f'{a}*{b}={ret}')
print()