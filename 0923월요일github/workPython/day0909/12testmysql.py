# 12testmysql.py

# mysql데이터베이스 
import pymysql
import time
       
config={
  'host' : '127.0.0.1' ,  
  'user' : 'root',
  'password' : '1234',
  'database' : 'naver' ,
  'port' : 3306
}

CN = pymysql.connect(**config)
cursor = CN.cursor()

def testSelectAll(): #사용자정의함수기술 리턴값x, 매개인자x
    # msg = "select * from test"
    cursor.execute("select * from test order by code")
    rows = cursor.fetchall()

    print()
    for r in rows:
        print(r[0], r[1], r[2], r[3] )
        #print('%4d\t %12s\t %3d\t %8s' %r)


def testInsert():  
    # code | name | hit  | today
    dcode = int(input('코드입력>>> '))
    dname = input('이름입력>>> ')
    msg = f"insert into test values({dcode}, '{dname}', 0, now())"
    cursor.execute(msg)
    CN.commit()
    print(dcode, '등록 저장 성공했습니다')


#=============================================================
while True:
    print()
    sel = int(input('1등록 2전체출력 3수정 4삭제 5이름조회 9종료>>>'))
    if sel == 9:
        break
    elif sel == 1:  
        print('test테이블 신규등록 처리입니다')
        testInsert()
        testSelectAll()
    elif sel == 2: #전체출력 
        time.sleep(0.5)
        testSelectAll()
    elif sel == 3: #수정 update ~ where
        pass
    elif sel == 4: #삭제 delete ~ where 
        pass
    elif sel == 5: #이름조회  where name like  '%키워드%'
        pass
    else:
        print('작업번호를 잘못 선택하셨군요\n')
    


# web웹태그+css = 방명록,게시판,인스타 가능
# web웹태그 code,name,title,조회수,날짜,이미지
  # 댓글기능까지 있으면 완벽한 프로그램
  # 로그인처리 userid,password
print('- ' * 50)
print()