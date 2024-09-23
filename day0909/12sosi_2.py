# 12sosi.py. 영임쌤
# 오라클 sosi테이블 + 파이썬

import os
import pandas as pd
import cx_Oracle    
import time
       
config = {
    'user' : 'system',
    'password' : '1234',
    'dsn' : '127.0.0.1:1521/xe'
}

CN = cx_Oracle.connect(**config) 
cursor = CN.cursor()


def sosiInsert():
    dcode = int(input('코드 입력>> '))
    message = f"select count(*) cnt from sosi where code = {dcode}"
    cursor.execute(message)
    cnt = cursor.fetchone()[0]
    if cnt != 0:
        print(dcode, '코드데이터는 이미 등록된 코드입니다')
        print('code 정확한 데이터를 입력하세요')
        #break  while,for반복문이 없어서 break단독기술에러 
        return  #return명령어 단독기술하면  함수탈출 
        print('우리나라 db처리 관련없는 처리구현 ')
        print('대한민국 db처리 관련없는 처리구현 ')
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
    length=len(rows)
    if length==0:
        return
  
    print('%s\t %8s\t %10s\t  %4s\t %6s\t %s' %('코드','이름','제목','급여','날짜','등급') )
    for r in rows:
        print('%4d\t %10s\t %10s\t  %4d\t %6s\t %s' %r) 
    print('전체데이터 갯수:' , len(rows))
    print('- ' * 50)
    print()
    time.sleep(1)



def sosiSelectTitle():
    #각자 조회갯수 출력
    print('제목데이터 like조회처리입니다 ')
    dtitle=input('제목조회>>>')
    msg1= f"select*from sosi where title like '%{dtitle}%' "
    # 에러msg2= f"select*from sosi where title like = '%{dtitle}%' "
    print()

def sosiDelete():
    sosiSelectAll() 
    print('code 데이터필드값으로 삭제처리')
    dcode = int(input('삭제코드 입력>> '))
    message = f"select count(*) cnt from sosi where code={dcode}"
    cursor.execute(message)
    cnt = cursor.fetchone()[0]
    if cnt == 0:
        print(dcode, '코드데이터는 미등록 삭제데이터입니다\n')
    else:
        msg = f"delete from sosi where code = {dcode}"
        cursor.execute(msg)
        CN.commit()
        print(dcode, '코드데이터 삭제처리 성공했습니다 ')
    sosiSelectAll() 


def sosiUpdate(): #수정갱신 update set where code 
    sosiSelectAll() 
    dcode = int(input('수정대상 코드 입력>> '))
    message = f"select count(*) cnt from sosi where code={dcode}"
    cursor.execute(message)
    cnt = cursor.fetchone()[0]
    if cnt == 0:
        print(dcode, '코드데이터는 미등록 갱신데이터입니다\n')
    else:
        #code,name필드 수정대상X title,sal,wdate, grade 4개필드 수정 
        dtitle = input('수정제목 입력>> ')
        dsal = int(input('수정급여 입력>> '))
        dgrade = input('수정등급 입력>> ')
        msg=f"update sosi set title='{dtitle}', sal={dsal}, wdate=sysdate, grade='{dgrade}' where code={dcode}"
        cursor.execute(msg)
        CN.commit()
        print(dcode, '코드데이터 수정처리 성공했습니다 ')

        sosiSelectAll() 



# 클래스 작성로 생략가능, 처리단위를 함수작성 + try~except예외
# while True:
#     print('1등록  2전체출력 3수정 4삭제 5제목조회 9종료>>> ')
#     #sel = int(input('1등록  2전체출력 3수정 4삭제 5제목조회 9종료>>> '))
#     break



sosiUpdate()
print()






'''
# 처음 작성 코드 09월 09월 월요일
# 12sosi.py
# 오라클 sosi테이블 + 파이썬
import os
import pandas as pd
import cx_Oracle  

# pip install oracledb 
import oracledb     
import time
       

config = {
    'user' : 'system',
    'password' : '1234',
    'dsn' : '127.0.0.1:1521/xe'
}


# CN = oracledb.connect(**config) #오류
# CN = oracledb.connect(user='system', password='1234', dsn='127.0.0.1:1521/xe') #오류
CN = cx_Oracle.connect(**config) 
#주석 print('config매개인자타입 ', type(config))
# 정답CN = cx_Oracle.connect(user='system', password='1234', dsn='127.0.0.1:1521/xe') #오류
cursor = CN.cursor()

print("database version: ", CN.version)
print("oracle connect ok success")
print()


def sosiInsert():
    print('sosi테이블 신규등록 처리 ')
    dcode = int(input('코드 입력>> '))
    message = f"select count(*) cnt sosi where code = {dcode}"
    
    #코드데이터 입력후 code필드값 중복체크/함수탈출/code재입력 
    #Error이유 unique constraint (SYSTEM.SYS_C007007) violated
    #1신규등록  2전체출력  3수정  4삭제  5제목조회  9종료
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
    #주석print('rows타입 ', type(rows))
    print()

    print('%s\t %8s\t %10s\t  %4s\t %6s\t %s' %('코드','이름','제목','급여','날짜','등급') )
    for r in rows:
        #비권장 print(r[0],r[1],r[2],r[3],r[4],r[5])
        print('%4d\t %10s\t %10s\t  %4d\t %6s\t %s' %r) 
    print('전체데이터 갯수:' , len(rows))
    print()




def sosiSelectTitle():
    pass
    print('제목데이터 like조회하세요 ')


def sosiDelete():
    pass
    print('code조회후 삭제처리하세요')


sosiSelectAll()
time.sleep(1)
sosiInsert()
sosiSelectAll()
# print()
'''