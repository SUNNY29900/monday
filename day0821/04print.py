#04print.py

#변수 하나씩 선언, 다중선언

a, b, ret = 9, 4, 0
msg=1234 

ret=a*b
print('|{}|*|{}|=|{}|'.format(a,b,ret))

print('|{}|'.format(msg))
print('|{:0>10,}|'.format(msg))           
print('|{:*>10,}|'.format(msg))          
print('|{:,}|'.format(msg))  




