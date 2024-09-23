# homewoklottoset.py

import random 

# 로또 1~45사이 숫자
# 숫자 중복체크
# 리스트대신 set사용 

lotto = [ ]
while len(lotto) != 6:
    lotto.append(random.randint(1,45))
    for k in range(len(lotto)) :
        if (lotto.count(lotto[k]) > 1) :
            lotto.pop() 
            lotto.append(random.randint(1,45))

print(lotto)
lotto.sort()
print(lotto)    

print()
print()


''' 나중에 리스트대신 set타입으로 변환'''
myset = { 7, 29, 45, 3 ,36, 12 }
print(myset)

