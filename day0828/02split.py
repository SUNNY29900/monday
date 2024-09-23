#02spilt.py

url='www.google.com'
print(url)

myret=url.split(',')  #ret=result/ 중복 피해  my   / #자동으로 리스트화
print(myret)     #리스트 ['www,google,com'] / 문자열 리스트화 할때 가장 쉽게 할 수 있는 방법
print(url.split(','))
print(list(url)) #글자를 하나 하나 쪼갬 ['w', 'w', 'w', '.', 'g', 'o', 'o', 'g', 'l', 'e', '.', 'c', 'o', 'm']  #비권장
print(url.split('.'))


print()


# url='www.google.com'
# print(url)

# myret=url.split('.')  #ret=result/ 중복 피해  my   / #자동으로 리스트화
# print(myret)     #리스트 ['www,google,com'] / 문자열 리스트화 할때 가장 쉽게 할 수 있는 방법
# print(url.split('.'))

# print()