# 03play.py
import time
import game #물리적인 파일이름만 명시

print('03play 사용문서')
time.sleep(1)

print(game.user_id)
print(game.user_pwd)

time.sleep(1)
game.terran()

time.sleep(1)
game.LG('gram')

time.sleep(1)
miter = game.running()
print('코스길이 ', miter)
print('코스길이 ', game.running())

# game.py문서
# 전역변수 user_id, user_pwd
# terran() LG(lg) running()리턴값있음






print()