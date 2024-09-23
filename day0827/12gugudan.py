#12gugudan.py문서 함수

# 파이썬 함수 def 함수이름():
# 파이썬 함수 매개인자

import time
def gugudan(name, dan):
   print('저자는', name)
   for k in range(1,10,1):
       print(f'{dan}*{k}={k*dan}')
       time.sleep(0.3)

mydata=0
try:
    mydata=int(input('단입력>>>'))
except:
    print('정수 숫자를 입력하세요(1~9사이를 숫자를 입력하세요)\n')

gugudan('슬기', mydata)  
print()

