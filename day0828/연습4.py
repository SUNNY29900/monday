#08jumin.py

import datetime
import time

jumin='971230-1835064'

#문제 1 성별체크  1/3 남자   2/4여자
# 주민등록번호의 7번째 자리를 통해 성별 확인
gender_code = jumin[7]
if gender_code in '1/3':
    gender = '남자'
elif gender_code in '2/4':
    gender = '여자'
else:
    gender = '알 수 없음'

print(f'성별: {gender}')
print('-'*50)


#문제 2 생일  12월 30일  생일 축하합니다
import datetime
# 주민등록번호의 생일 부분을 추출
birth_date = jumin[:6]  # '971230'
birth_day = datetime.datetime.strptime(birth_date, '%y%m%d').strftime('%Y년 %m월 %d일')

print(f'생일: {birth_day} 생일 축하합니다!')
print('-'*50)
print()
print()

#문제 3 나이계산 2024-1997=???
# 현재 연도와 출생 연도를 통해 나이 계산
current_year = datetime.datetime.now().year
birth_year_prefix = '19'  # 기본값으로 '1900년대' 가정
if gender_code in '34':  # 2000년대 출생인 경우
    birth_year_prefix = '20'

birth_year = int(birth_year_prefix + jumin[:2])  # '1997'
age = current_year - birth_year

print(f'나이: {age}세')
print('-'*50)

jum1='971230'    #len() 6자릿수 체크
jum2='1835064'   #len() 7자릿수 체크

'''
문자열을 주석사용:안내문 역할 #''''''. """" 주석처리
dt= datetime.datetime.now()   #정답

print(str(dt)[0:4]) #2024-2001=나이계산


mytime=time.localtime()
print(mytime.tm_year)   #2024년도 나이계산
'''  