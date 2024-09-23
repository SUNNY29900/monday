# 12dict.py

mysite = dict()

mysite['insta'] = 'www.insta.com'
mysite['kakao'] = 'www.kakao.net'
mysite['naver'] = 'www.naver.com'

print(mysite)
print()

print(mysite.keys())   #키값목록
print()

print(mysite.values()) #value값목록
print()

print(mysite['kakao'])

#for반복문
# for key in mysite:
#     print(key, ':', mysite[key])