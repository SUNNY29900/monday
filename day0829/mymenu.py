#09dictmenu.py
#예외처리 try:~~except: ~~생략
import time
import sys  #프로그램 종료 sys.exit()
from datetime import datetime        #기술하면 datetime.now()
import datetime   #datetime.datetime.now()

menu=dict()
flag=True
num, su, sel=0,0,0
msg, info, message='안내문', '안내', '안내메'

dt= datetime.datetime.now()
print('처리날짜', datetime.datetime.now())
print('처리날짜', dt)
print()


def menuInsertNew():
    name=input('이름입력key>>>')
    price=input('가격입력value>>>')
    menu[name]=price
    print(name, '등록성공했습니다')


def menuAllprint():
    for i, k in enumerate (menu):
        print(i, k, '', menu[k])
    print()



def menuEditupdate():
    name=input('편집대상 키값 입력>>>')
    if menu.get(name)==None:
            print('편집대상 딕트가  key 없습니다')
    else:
            price=input('변경 가격 재입력 value>>>')
            menu[name]=price
            print(name, '가격수정편집 성공했습니다')


def menuDelete():
    name=input('삭제대상 키값 입력>>>')
    if menu.get(name)==None:
            print('삭제대상 딕트가 key없습니다')
    else:
        menu.pop(name)
        print(name, '데이터삭제 성공했습니다')
        time.sleep(0.3)
        for k,v in menu.items():
            print( k ,' ', v)


def menuFindsearch():
    key = input('조회검색 key 입력>>> ')
    if menu.get(key) == None:
        print(key, '데이터가 없습니다')
    else:
        print(key, menu[key],'데이터 조회성공했습니다') 


def menuExit():
    print('딕트처리를 종료합니다\n')
    flag = False 


#-----------------------------------------------
while flag:
    print()
    num=int(input('1등록 2출력 3수정 4삭제 5조회 9종료>>>'))
    if num ==9:menuExit()
    elif num ==1: menuInsertNew()
    elif num ==2: menuAllprint()
    elif num ==3: menuEditupdate()
    elif num ==4: menuDelete()
    elif num ==5: menuDindserrch()

    else:print('처리번호를 잘못 입력하였습니다\n')






