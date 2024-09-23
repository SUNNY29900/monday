#08jumin.py

import datetime
import time

jumin='971230-1835064'

#문제 1 성별체크  1/3 남자   2/4여자



#문제 2 생일  12월 30일  생일 축하합니다




#문제 3 나이계산 2024-1997=???
import datetime

userName = input("이름을 입력해주세요 : ")

userBirthYear = int(input("친태어난 년도를 입력해주세요(ex:1990) : "))
userBirthMonth = int(input("태어난 월을 입력해주세요(ex:3) : "))
userBirthDay = int(input("태어난 일을 입력해주세요(ex:10) : "))

thisYear = datetime.date.today().year
thisMonth = datetime.date.today().month
thisDay = datetime.date.today().day

print("%s 님의 한국나이는 현재(%d년) %d세 이고," %(userName, thisYear, thisYear - userBirthYear + 1))

isBirthdayPassed = False

if(thisMonth > userBirthMonth) :
    isBirthdayPassed = True
elif(thisMonth == userBirthMonth) :
    if(thisDay >= userBirthDay) :
        isBirthdayPassed = True
    else :
        isBirthdayPassed = False
else :
    isBirthdayPassed = False;

if(isBirthdayPassed == True) :
    print("만 나이는 %d세 입니다." %(thisYear - userBirthYear))
else :
    print("만 나이는 %d세 입니다." %(thisYear - userBirthYear - 1))



print()
print()