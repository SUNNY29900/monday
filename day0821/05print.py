#05print.py

#변수 선언

msg=97234 
print('{}'.format(msg))                 #정석
print('{:>10,}'.format(msg))            #총10자릿수 >오른쪽 맞춤
print('{:<10,}'.format(msg))            #총10자릿수 <왼쪽 맞춤
print('{:^10,}'.format(msg))            #총10자릿수 ^중앙 맞춤

print('-' *100)                         #-는 문자열을 반복한다는 뜻
print('{:0>10,}'.format(msg))           #000097,234
print('{:*>10,}'.format(msg))           #****97,234
print('{:,}'.format(msg))               #97,234



