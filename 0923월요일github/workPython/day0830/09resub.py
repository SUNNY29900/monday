# 09resub.py

import re

phone = '010-7800-1234 박이썬'
# 힌트 re.sub( '1패턴', '2변경적용', phone)
model = re.sub( '-[0-9]{4}-'  , '-****-' ,  phone)

print(phone)  # 010-7800-1234 박이썬
print(model)  # 010-****-1234 박이썬
 
# 1번째 정규식 예제 re.findall()
# msg = 'my best %#@& 245 오렌지 is (_^!& ^.^ 수박 cherry as tea'
# result1 = re.findall('[\w]+' , msg)
# result2 = re.findall('[\W]+' , msg) #비권장
# result3 = re.findall('[a-zA-Z0-9가-힣]+' , msg)
# result4 = re.findall('[^a-zA-Z0-9가-힣]+' , msg)
# print(result1); print()
# print(result2); print()
# print(result3); print()
# print(result4); print()


# 2번째 정규식 예제 re.findall()
# msg='my best blue myjava my cherry blue mypython my'
# x = re.findall('my' ,msg)
# y = re.findall('blue' ,msg)
# z = re.findall('red' ,msg)
# print(x)
# print(y)
# print(z) #에러대신[]출력
# print()


# 첫번째 정규식 예제 re.findall()
# msg = 'my best% 2400 Flu_it  is  blue%#357cherry'    
# info1 = re.findall('[a-zA-Z]{3,7}' , msg)
# info2 = re.findall('[a-zA-Z0-9]{3,7}' , msg)
# print(info1) ['best', 'Flu', 'blue', 'cherry']
# print(info2) ['best', '2400', 'Flu', 'blue', '357cher']

print()