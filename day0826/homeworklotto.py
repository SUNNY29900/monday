#연습
import random

lotto = []  # 로또 번호를 저장할 리스트

while len(lotto) < 6:  # 리스트에 6개의 번호가 들어갈 때까지 반복
    num = random.randint(1, 45)  # 1부터 45까지의 랜덤 숫자 생성
    
    if num not in lotto:  # 생성된 숫자가 리스트에 없는 경우
        lotto.append(num)  # 리스트에 숫자를 추가
    # 중복된 숫자가 리스트에 있으면 아무 작업도 하지 않음

# 리스트를 오름차순으로 정렬
lotto.sort()

# 결과 출력
print("로또 번호:", lotto)