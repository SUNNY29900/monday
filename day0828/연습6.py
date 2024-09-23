# 입력받기
year = int(input("년(year)>>> "))
month = int(input("월(month)>>> "))
day = int(input("일(day)>>> "))

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