# 06re.py

import re

# url = 'www.google.com'
# print(url.split('.'))#['www', 'google', 'com']              
# print(' '.join(url)) #w w w . g o o g l e . c o m

msg = 'my best% 2400 Flu_it  is  blue%#357cherry'    

info1 = re.findall('[a-zA-Z]{3,7}' , msg)
info2 = re.findall('[a-zA-Z0-9]{3,7}' , msg)
print(info1)
print(info2)
print()

my = re.findall('[a-zA-Z]{4,10}' , msg)
if my :
    print(my)
else:
    print('[a-zA-Z]{7,10} 조건에 맞는 데이터 없습니다')

# msg = 'my best% 2400 Flu_it  is  blue%#357cherry'








print()