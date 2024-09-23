# 04gugudanfor.py 

import time

dan = int(input('원하는 단입력>>> ')) 
for k in range(1,10,1):
    print(f'{dan}*{k}={dan*k}')
    time.sleep(0.3) 


print()

#예제1
dan=3
for k in range(1,10,1):
   print(f'{dan}*{k}={dan*k}')
print()