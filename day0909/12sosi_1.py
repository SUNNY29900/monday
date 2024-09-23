# 12sosi.py

# 오라클 sosi테이블 + 파이썬
import os
import pandas as pd
import cx_Oracle  

# # pip install oracledb 
# import oracledb     
import time
       

config = {
    'user' : 'system',
    'password' : '1234',
    'dsn' : '127.0.0.1:1521/xe'
}


CN = cx_Oracle.connect(**config) 
cursor = CN.cursor()

def sosiInsert():
    print('sosi테이블 신규등록 처리 ')
    dcode = int(input('코드 입력>> '))
    msg = f"select count(*) cnt from sosi where code= {dcode}"
    cursor.execute(msg)
    cnt=cursor.fetchone()[0]
    # check =len(cnt)
    # print('cnt타입', cnt)
    if cnt != 0:
        print(dcode, '코드데이터는 이미 등로된 코드입니다')
        print('code 정확한 데이터를 입력하세요')
        #break #while, for  반복문이 없어서 break 단독 기술에러
        return  #리턴문장 단독기술하면 함수탈출
        print('우리나라 db처리 관련없는 처리구현')
        print('대한민국 db처리 관련없는 처리구현')
    else:
       dname = input('이름 입력>> ')
       dtitle = input('제목 입력>> ')
       dsal = int(input('급여 입력>> '))
  
       msg = f"insert into sosi values({dcode},'{dname}','{dtitle}',{dsal}, sysdate, 'C')"    
       cursor.execute(msg)
       CN.commit()
       print(dcode , ' 저장 성공했습니다')
       time.sleep(1)


def sosiSelectAll():
    msg = "select * from sosi order by code"
    cursor.execute(msg)
    rows = cursor.fetchall()
    #print('rows타입 ' ,type(rows) )
    #print()
  
    print('%s\t %8s\t %10s\t  %4s\t %6s\t %s' %('코드','이름','제목','급여','날짜','등급') )
    for r in rows:
        print('%4d\t %10s\t %10s\t  %4d\t %6s\t %s' %r) 
    print('전체데이터 갯수:' , len(rows))
    print('- ' * 50)
    print()
    time.sleep(1)

    #   CODE NAME  TITLE   SAL WDATE    GRADE
    #   ------ ----------- ------ ----- --------
    #  3300 three                cake                     96 24/09/06 D
    #  2200 kim                  two                      92 24/09/06 D


def sosiSelectTitle():
    pass
    print('제목데이터 like조회하세요 ')


def sosiDelete():
    print('code 데이터 필드 값으로 삭제처리')
    dcode = int(input('코드 입력>> '))
    meg = f"select count(*) cnt from sosi where code= {dcode}"
    cursor.execute(meg)
    cnt=cursor.fetchone()[0]
    if cnt != 0:
        print(dcode, '코드데이터는 이미 등로된 코드입니다')
        print(dcode, '데이터 삭제대상이 아닙니다')
        
    else:
      msg="delete~~where code"



# while True:
#     print('1등록  2전체출력 3수정 4삭제 5제목조회 9종료>>> ')
#     #sel = int(input('1등록  2전체출력 3수정 4삭제 5제목조회 9종료>>> '))
#     break


# sosiSelectAll()
time.sleep(1)
sosiInsert()
print()
time.sleep(0.5)

# 
time.sleep(1)
print()

sosiDelete()   #삭제처리 3시 10분까지 삭제처리하세요



"""
#처음 작성 코드 09월 9일 월요일


# 오라클 sosi테이블 + 파이썬
import os
import pandas as pd
import cx_Oracle  

# # pip install oracledb 
# import oracledb     
import time
       

config = {
    'user' : 'system',
    'password' : '1234',
    'dsn' : '127.0.0.1:1521/xe'
}


# CN = oracledb.connect(**config) #오류
# CN = oracledb.connect(user='system', password='1234', dsn='127.0.0.1:1521/xe') #오류
CN = cx_Oracle.connect(**config) 
# print('config매개인자 ', type(config))
cursor = CN.cursor()

print("database version: ", CN.version)
print("oracle CNect ok success")
print()


def sosiInsert():
    print('\nsosi테이블 신규등록 처리 ')
    dcode = int(input('코드 입력>> '))
    message = f"select count(*) cnt sosi where code= {dcode}"

    #코드데이터 입력 후 code 필드값 중복체크/ 함수탈출/ code재입력
    #에러이유  unique constraint (SYSTEM.SYS_C007077) violated
    # 1. 신규등록, 2전체등록 3수정 4삭제 5제목조회 9 종료 
    dname = input('이름 입력>> ')
    dtitle = input('제목 입력>> ')
    dsal = int(input('급여 입력>> '))
  
    #신규등록하기 전에 select ~~~

    msg = f"insert into sosi values({dcode},'{dname}','{dtitle}',{dsal}, sysdate, 'C')"    
    cursor.execute(msg)
    CN.commit()
    print(dcode , ' 저장 성공했습니다')
    time.sleep(1)




def sosiSelectAll():
    msg = "select * from sosi order by code"
    cursor.execute(msg)
    rows = cursor.fetchall()
    # print('rows타입 ', type(rows))
    print()

    #제목 print('%s\t %s\t %10s\t  %4s\t %6s\t %s' %('코드','이름','제목','등급','날짜','급여') )
    for r in rows:
        # 비권장 print(r[0],r[1],r[2],r[3],r[4],r[5])
        print('%d\t %8s\t %10s\t  %4d\t %6s\t %s' %r) 
    print('전체데이터 갯수:' , len(rows))
    print('- ' * 50)
    time.sleep(1)

    #   CODE NAME  TITLE   SAL WDATE    GRADE
    #   ------ ----------- ------ ----- --------
    #  3300 three                cake                     96 24/09/06 D
    #  2200 kim                  two                      92 24/09/06 D


def sosiSelectTitle():
    pass
    print('제목데이터 like조회하세요 ')


def sosiDelete():
    pass
    print('code조회후 삭제처리하세요')


sosiSelectAll()
def sosiSelectAll():
    msg = "SELECT * FROM sosi ORDER BY code"
    cursor.execute(msg)
    rows = cursor.fetchall()
    return row  # 데이터를 반환하도록 수정
print()



def sosiSelectAll():
    msg = "SELECT * FROM sosi ORDER BY code"
    cursor.execute(msg)
    rows = cursor.fetchall()
    result_dict = {row[0]: row for row in rows}  # code를 키로 하는 딕셔너리 생성
    return result_dict



while sosiSelectAll:
    print()
    num=int(input('1등록 2출력 3수정 4삭제 5조회 9종료>>'))
    if num == 9:
        print('딕트처리를 종료합니다\n')
        sosiSelectAll.exit()
# 09dictmenu.py
# 예외처리 try: ~~~ except: ~~~ 생략
import time
import sys  #프로그램종료 sys.exit()

menu = dict()
flag = True
num,su,sel = 0,0,0
msg,info,message = '안내메', '안내메', '안내메'

while flag:
    print()
    num=int(input('1등록 2출력 3수정 4삭제 5조회 9종료>>'))
    if num == 9:
        print('딕트처리를 종료합니다\n')
        #break 
        #flag = False 
        sosiSelectAll.exit()

    elif num == 1: 
        name = input('이름입력key>>>')
        code = input('가격입력value >>>')
        menu[name] = code
        print(name, '등록 성공했습니다')

    elif num == 2:  
        for k,v in menu.items():
            print( name ,' ', code)
        print()
    elif num == 3:  
        name = input('편집대상 키값 입력>>> ')
        if menu.get(name) == None:
            print('편집대상 딕트가 key 없습니다')
        else:
            price = input('변경가격 재입력value >>>')
            menu[name] = code
            print(name, '가격수정편집 성공했습니다')

    elif num == 4: 
        name = input('삭제대상 키값 입력>>> ')
        if menu.get(name) == None:
            print('삭제대상 딕트가 key 없습니다')
        else:
            menu.pop(name)
            print(name, '데이터삭제 성공했습니다')
            time.sleep(0.3)
            for name,code in menu.items():
                print( k ,' ', v)
                
    elif num == 5: 
        key = input('조회검색 key 입력>>> ')
        if menu.get(key) == None:
            print(key, '데이터가 없습니다')
        else:
            print(key, menu[key],'데이터 조회성공했습니다')
    else:
        pass
        print('처리번호를 잘못 입력하셨네요\n')
         

sosiInsert()
time.sleep(0.5)
sosiSelectAll()
#print()



"""

