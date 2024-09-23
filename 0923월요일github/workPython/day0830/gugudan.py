# gugudan.py

# 함수 4개작성
# 시작 진입 호출 main 
# main함수 toptitle(), guguinput(), guguoutput(), endtitle()호출
# 출력  time.sleep(1)
# 입력  input() 이용, 형변환

from time import sleep,localtime  # import time   사용  time.sleep(1)

def toptitle():
    print()
    print('mygugudan 처리')
    print('-' * 30)

def endtitle():
    print('-' * 30)
    print()


def guguinput():
    dan = 1 #지역변수
    try:
        dan = int(input('단입력>>>'))
    except Exception as ex:
        print('에러이유 ', ex)
    return dan 


def guguoutput(dan):
    for k in range(1,10,1):
        print(f'{dan} * {k} = {dan*k}')
        sleep(1)


def main():
    toptitle()
    data = guguinput()
    guguoutput(data)
    endtitle()


# 진입함수호출
main()







print()