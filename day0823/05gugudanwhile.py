#05gugudanwhile.py
import time

data=input('원하는 단입력>>>')   
dan=int(data)

k=1
while True:
    print(f'{dan}*{k}={dan*k}')
    k=k+1
    time.sleep(0.5)
    if k>9:
        break

print()

#예제1
import time

dan=3
k=1
while k<=9:
    print(f'{dan}*{k}={dan*k}')
    k=k+1
    time.sleep(0.5)

print()

