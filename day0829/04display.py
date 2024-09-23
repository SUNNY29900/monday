#04display.py

import time
# import 문서이름
# 참조할때 game.user_pwd, game.terran()
# from 문서이름 import 전역변수, 함수이름만

from game import user_id, user_pwd, terran
from game import LG, running
print('04display.py')

time.sleep(1)

print(user_id)
print(user_pwd)

time.sleep(1)
terran()

time.sleep(1)
LG('그램')

time.sleep(1)
miter=running(4500)
print('코스길이', miter)
print('코스길이', running())

# game.py문서
# 전역함수 user_id, user_pwd
# terran() LG(lg)  running()리턴값 있음

