#p7exceptinput.py
#문제1) dan입력 키보드 input(),  형변환
import time
dan=int(input('원하는 단 입력>>>'))
for k in range (1,10,1):
    print(f'{dan}*{k}={dan*k}')
    time.sleep(0.3)

print()

#문제2) 예외처리  try :~except
import time
dan=0 #초기값
try: 
    pass
    dan=int(input('원하는 단 입력>>>'))
except:
    pass
for k in range (1,10,1):
    print(f'{dan}*{k}={dan*k}')
    time.sleep(0.3)


#문제3) dan 입력 범위 정수 1이상, 2~9사이
#1건이상처리는 무조건 반복문
import time
dan=0 #초기값
try: 
    pass
    dan=int(input('원하는 단 입력>>>'))
    if dan <2 or dan>9:
       pass
       print('숫자범위는 2~9사이 숫자입니다\n다시 입력하세요')
except:
    pass
for k in range (1,10,1):
    print(f'{dan}*{k}={dan*k}')
    time.sleep(0.3)




import time

dan=3
for k in range (1,10,1):
    print(f'{dan}*{k}={dan*k}')
    time.sleep(0.5)

print()
time.sleep(0.5)
print('포인트 7점 획득')
print('포인트 5점이상이면 vip자격만족대상입니다')

print()
print('-'*50)


