#08testdatatime.py

import time
import datetime

my=time.localtime()
print(my)
print(my.tm_year,'년')
print(my.tm_mon,'월')
print(my.tm_mday,'일')
print(my.tm_wday)   #0월요일   1화요일   2수요일    3목요일  4금요일
time.sleep(0.5)
print()

dt=datetime.datetime.now()
print(dt)   #2024-08-23 11.15:59.699633
print()

time.sleep(0.5)
print('aaaaaaaa')
time.sleep(0.5)
print('bbbbbbbbb')
time.sleep(0.3)
print('ccccccccc') 
time.sleep(0.3)
