#gugudan.py


# #함수  4개 작성

# 시작 진입 호출 main
# main함수   toptitle()호출, gugudinput(), output(), undertitle()호출

# 출력 time.sleep(1)

# 입력   input()  이용, 형변환 

from time import sleep, loocaltime   #import time  사용  time. sleep(1)

def title():
    print('mygugudan  처리')
    print('-'*30)


def endtitle(): 
    print('-'*30)
    print()

def guguinput():
    #반드시 리턴처리
    d=1    #지역변수
    try:
       dan=int(input('단입력>>>'))
    except Exception as ex: 
       print('에러이유', ex)
    return dan
   #리턴값

def gugudan(dan):


def guguoutput(dan):
    for k in range(1,11,1):
    #for반복문  
    print(f'{dan}*{k}={dan*k})
    sleep(1)
    #매개인자


def main():
    #진입=시작   매개인자 x, 리턴값x
    toptitle()
    data=guguinput()   #리턴값 필수
    guguoutput( data)    #매개인자 필수
    endtitle()         #


    #진입함수 호출

    main()



    print()

