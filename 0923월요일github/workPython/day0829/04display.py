# 04display.py

import time

# import 문서이름 
  #참조할때  game.user_pwd,  game.terran()
# from 문서이름 import 전역변수,함수이름만
from game import user_id, user_pwd, terran
from game import LG, running


print(user_id)
print(user_pwd)

terran()
LG('gram')

miter = running()
print('코스길이 ', miter)
print('코스길이 ', running())



# game.py문서
# 전역변수 user_id, user_pwd
# terran() LG(lg) running()리턴값있음
print()