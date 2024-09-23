#test.py


#day0829폴더\test.py

#문제1   name, age, gender 변수사용, 키보드입력input, 나이는 숫자                                  #문제1   name, age, gender 변수사용, 키보드입력input, 나이는 숫자
                                         
name= input('이름을 입력하세요:')                                                                 name=input('이름을 입력하세요:')
age=int(input('나이를 입력하세요:'))                                                              age=int(input('나이를 입력하세요'))
gender_input=input('성별을 입력하세요(남자/여자 또는 man/woman):') . strip().lower                 gender_input=input('성별을 입력하세요(남자/여자 또는 man/woman):'), strip(). lower
print(f'이름: {name}')                                                                           print(f'이름"{name}')
print(f'나이: {age}')                                                                            print(f'나이:{age}')
print(f'성별: {'gender'}')                                                                       print(f'성별: {'gender'}')
print()                                                                                          print()

# 문제2  나이입력 범위 20~70사이                                                                   # 문제2  나이입력 범위 20~70사이   조건 20미만 청소년 1~19  20~30청년  31~65 중년  66이상 노년
#          조건 20미만 청소년 1~19  20~30청년  31~65 중년  66이상 노년
if age <20:                                                                                     if age<20:
    age_catefory='청소년'                                                                            age_catefory='청소년'

elif 20<= age<=30:                                                                             elif 20<=age<=30:
    age_catefory='청년'                                                                               age_catefory='청년'
 
elif 31<= age<=65:                                                                             elif 31<=age<=65
    age_catefory='중년'                                                                              age_catefory='중년'

else:                                                                                           else:
    age_category = '노년'                                                                             age_catefory='노년'

print()                                                                                         print()

#문제3  남자/남/man입력  True 출력       여자/여/woman입력 False출력 
# print(홍길동)
# print(34, 청년)
# print(남자)

#고민 list관리 / tuple관리/ dicr관리
#이름 홍길동
#34세 청년
#성별 남자

#홍길동
# 24세 청년 
# 남자

#4. 예외처리 대상은 나이 try: ~except:
