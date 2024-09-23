#play.py
import time
import game   #물리적 파일이름만 명시
print('03play.py')


print('03play.py')
time.sleep(1)

print(game.user_id)
print(game.user_pwd)

time.sleep(1)
game.terran()

time.sleep(1)
game.LG('그램')

time.sleep(1)
miter=game.running(4500)
print('코스길이', miter)
print('코스길이', game.running())

# game.py문서
# 전역함수 user_id, user_pwd
# terran() LG(lg)  running()리턴값 있음

