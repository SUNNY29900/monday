#10.recompile.py

import re
data='''
kim  840916-1694852
lee  921207-2759327
tea  981024-1674938
'''

com=re.compile('-\d+')  
first=com.sub('-*******', data)
print(first)  #비권장 

two= re.sub('[0-9]{7}','*******',data)  #추천
print(two)

print()



#4번째 정규식 예제 re.sub(1,2,3)
# 힌트 re.sub('1패턴', '2변경 적용', phone)
# phone='010-7800-1234 박이썬'
# model=re.sub( '-[0-9]{4}-' , '-****-' , phone)
# print(phone)    #  출력값: 010-7800-1234 박이썬
# print(model)    #  출력값: 010-****-1234 박이썬













# #1번째 정규식 예제
# # msg 변수에 새로운 내용 원래내용 덮어씌우는 재할당
# msg= 'my best %#@& 245 오렌지 is (_^&^.^ 수박 cherry as tea'
# result1=re. findall('[\w]+', msg)    #+붙이며 word로 나옴/ #비권장 
# result2=re. findall('[\w]+', msg)
# result3=re. findall('[a-zA-Z0-9가-힝]+', msg)
# result4=re. findall('[^a-zA-Z0-9가-힝]+', msg)   #출력값 : [' ', ' %#@& ', ' ', ' ', ' (_^&^.^ ', ' ', ' ', ' ']
# print(result1); print()
# print(result2); print()
# print(result3); print()
# print(result4); print()
# print()

# 2번째 정규식 예제
# msg= 'mybest blue myjava my cherry blue mypython my '
# x=re.findall( 'my' , msg )
# y=re.findall( 'blue' , msg )
# z=re.findall( 'red' , msg )
# print(x)
# print(y)
# print(z)    #없으면 에러 대신  []  이런 형태로
# print()
