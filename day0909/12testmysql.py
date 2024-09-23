#12testmysql.py

#mysql 데이터베이스
import pymysql
import time

#Dtabase configuration
config = {
    'host' : '127.0.0.1',
    'user' : 'root',
    'password' : '1234',
    'database' : 'naver',
    'port' : 3306
}

#Connect to the database
CN = pymysql.connect(**config)   #Establishes a connection to the database
cursor = CN.cursor()              #Creates a cursor object to execute SQL

def testSelectAll():  
  msg = "select * from test "
  cursor.execute(msg)
  rows = cursor.fetchall()

  print()
  for r in rows:
     print(r[0], r[1], r[2], r[3] )
    #print('%4d\t %12s\t %3d\t %8s' %r)


def testInsert():
    #code|name|hit|today
    dcode = int(input('코드입력>>> '))
    dname = input('이름입력>>>')
    msg=f"INSERT INTO test (id, name, hit, today) VALUES ({dcode}, '{dname}', 0, NOW())"
    print(dcode, '등록저장 성공했습니다')
    #print('%4d'\t  %12s'\t   %6s'\t  %8s' %r) 



#----------------------------------------------------------------------

while True:
    print()
    sel= int(input('1. 등록 2. 전체출력 3. 수정 4. 삭제 5. 이름조회 9. 종료>>>'))
    if sel==9:
        break
    elif sel == 1:
        print('test테이블 신규등록 처리입니다') 
        testInsert()
        testSelectAll()
    elif sel == 2:          #전체출력    
       time.sleep(0.5)
       testSelectAll()     
    elif sel == 3:         #수정 update~where
        pass
    elif sel == 4:         #삭제  delete ~ where
        pass
    elif sel == 5:         #이름 조회 where name like  '%키워드%' 
        pass
    else:
        print('작업번호를 잘못 선택하셨군요\n')

# web웹태그 + css = 방명록, 게시판, 인스타
# web웹태그 code, name, title, 조회수 날짜 이미지
# 댓글 기능까지 있으면 완벽하 프로그램
# 로그인처리 userid, password
print('----'*50)
print()

