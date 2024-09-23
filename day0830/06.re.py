#06re.py

import re
# url='www.google.com'
# print(url.split(','))
# print(''.join(url))  

msg= 'mybest %  Flu_it is blue %357cherry'  #정규식으로 사용하면 list화가 됨-> ['mybest', 'Flu', 'blue', '357cher']
info1=re.findall('[a-zA-Z0-9]{3,7}', msg)    #
info2=re.findall('[a-zA-Z0-9]{3,7}', msg)
print(info1)
print(info2)
print()

# msg= 'mybest % 2400 Flu_it is blue %357cherry'    # 숫자빼고 싶을때357
# info1=re.findall('[a-zA-Z0-9]{3,7}', msg)    #
# info2=re.findall('[a-zA-Z0-9]{3,7}', msg)
# print(info1)
# print(info2)
# print()

my= re.findall('[a-zA-Z0-9]{7,9}', msg)
if my : 
    print(my)
else:
    print('[a-zA-Z0-9]{7,9} 조건에 맞는 데이터가 없습니다')

# msg= 'mybest % 2400 Flu_it is blue %357cherry' 



