# homeworkcoffee.py

money = int(input('금액입력 >>> '))

while True:
    print('----------')
    sel = int(input('1.커피(250) 2.코코아(200) 3.반환 9:종료 >>> '))

    if sel == 9:
        print("종료합니다.")
        break
    elif sel == 3:
        print("잔액 반환:", money)
        money = 0
    elif sel == 1 and money >= 250:
        money -= 250
        print(f'커피 주문 완료. 남은 잔액은 {money}입니다.')
    elif sel == 2 and money >=  200:
        money -= 200
        print(f'커피 주문 완료 남은 잔액은 {money}입니다.')
    else:
        print(f'잔액이 부족하거나 잘못된 선택입니다. 현재 잔액은  {money}입니다.') 




