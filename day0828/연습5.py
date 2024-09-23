import datetime

current_year = datetime.datetime.now().year   # 현재 연도 가져오기

jumin = '971230-1835064'   # 주민등록번호 입력 (예시)

# 주민등록번호에서 성별 코드 추출
gender_code = jumin[7]  # '-' 다음 첫 번째 문자 (성별 코드)

# 출생 연도의 접두사 결정
if gender_code in '12':
    birth_year_prefix = '19'
else:
    birth_year_prefix = '20'

# 출생 연도 계산
birth_year = int(birth_year_prefix + jumin[:2])  # '97' (연도 부분)

# 나이 계산
age = current_year - birth_year

print(f'나이: {age}세')
print('-'*50)