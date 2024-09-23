# 07re.py

import re

msg='my best blue myjava my cherry blue mypython my'
x = re.findall('my' ,msg)
y = re.findall('blue' ,msg)
z = re.findall('red' ,msg)
print(x)
print(y)
print(z) #에러대신[]출력
print()

# msg변수에 새로운내용 덮어씌우는 재할당
msg = 'my best %#@& 245 오렌지 수박 cherry as tea'

result1 = re.findall('[\w]' , msg)
result2 = re.findall('[\W]' , msg)
result3 = re.findall('[a-zA-Z0-9가-힣]' , msg)
print(result1)
print(result2)
print(result3)

# 첫번째 정규식 예제
# msg = 'my best% 2400 Flu_it  is  blue%#357cherry'    
# info1 = re.findall('[a-zA-Z]{3,7}' , msg)
# info2 = re.findall('[a-zA-Z0-9]{3,7}' , msg)
# print(info1) ['best', 'Flu', 'blue', 'cherry']
# print(info2) ['best', '2400', 'Flu', 'blue', '357cher']

print()