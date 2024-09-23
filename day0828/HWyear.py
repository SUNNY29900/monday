#HWyear.py

#함수없이 list, 중첩으로쓸 것인지  고민

day=[0 ,31, 28, 31, 30, 31, 30, 31, 31, 30, 30, 31]
year=int(input("년year>>>"))
month=int(input("월month>>>"))
date= int(input("일date>>>"))

# 리스트  day=[0 ,31, 28, 31, 30, 31, 30, 31, 31, 30, 30, 31]
# 리스트, 튜플, 문자열 없이 입력데이터로 if제어문
# if제어문 or/and  중첩


# 윤년 판별
is_leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# 윤년 여부 출력
if is_leap_year:
    print(f"{year}년은 윤년입니다.")
else:
    print(f"{year}년은 윤년이 아닙니다.")

# 월별 일 수 확인
if month < 1 or month > 12:
    print("잘못된 월입니다.")
elif month == 2:
    days_in_month = 29 if is_leap_year else 28
elif month in [4, 6, 9, 11]:
    days_in_month = 30
else:
    days_in_month = 31

# 날짜 유효성 검사
if day < 1 or day > days_in_month:
    print("잘못된 일입니다.")
else:
    print(f"{year}년 {month}월 {day}일은 유효한 날짜입니다.")


'''
  윤년 기준
  1. 4의 배수
  2. 100의 배수가 아닌 4의 배수
  3. 400의 배수

'''
# 2024  2 입력하면 윤년입니다. 
# 2024년 2월 29일/ 2020년 2월 29일 
# 2021년 2022년 2023년 28일  


#kim 840916-*******
#lee 840916-*******
#goo 840916-*******
data='''
#kim 840916-1094
#lee 840916-*******
#goo 840916-*******
'''
