# homeworkcoffee.py

money = int(input('금액입력 >>> '))

while True:
    print('---')
    sel = int(input('1.커피(250)  2.코코아(200)  3.반환  9:종료 >>> '))

    if sel == 9:
        print("종료.")

    elif sel == 3:
        print("잔액 반환:", money)
        money = 0

    elif sel == 1 and money >= 250:
        money -= 250
        print(f'커피 주문 완료. 남은 잔액은 {money}')
 
    elif sel == 2 and money >= 200:
        money-=200
        print(f'코코아 주문 완료. 남은 잔액은 {money} ')
 
    else:
        print("잔액이 부족 또는 잘못된 선택. 현재 잔액: money" )


