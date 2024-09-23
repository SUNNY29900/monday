import time
import pymysql

# Database connection configuration
config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': '1234',
    'database': 'naver',
    'port': 3306
}

# Connect to the database
CN = pymysql.connect(**config)
cursor = CN.cursor()

def goodsInsert():
    dcode = int(input('코드 입력>> '))
    message = f"select count(*) cnt from goods where code = {dcode}"
    cursor.execute(message)
    cnt = cursor.fetchone()[0]
    
    if cnt != 0:
        print(dcode, '코드데이터는 이미 등록된 코드입니다')
        print('code 정확한 데이터를 입력하세요')
        return  # 함수 종료
    
    dname = input('이름 입력>> ')
    dsu = int(input('수량입력>> '))
    ddan = int(input('단가입력>> '))

    msg = f"insert into goods (code, name, su, dan) values({dcode}, '{dname}', {dsu}, {ddan})"    
    cursor.execute(msg)
    CN.commit() 
    print(dcode, ' 저장 성공했습니다')
    time.sleep(1)

def goodsSelectAll():  # 전체출력
    msg = "SELECT * FROM goods ORDER BY code"
    cursor.execute(msg)  # SQL 쿼리 실행
    rows = cursor.fetchall()
    
    print('%s\t %8s\t %10s\t %4s\t %6s\t %s' % ('idx', 'code', 'name', 'su', 'dan', 'wdate'))
    
    for r in rows:
        print('%s\t %10s\t %10s\t %4d\t %6s\t %s' % r)
    
    print('전체 데이터 갯수:', len(rows))  # 전체 데이터 갯수 출력
    print('_' * 50)
    time.sleep(1)


def goodsDelete(): 
    goodsSelectAll()
    print()
    decode = input('삭제코드 입력>>> ')  # 문자열로 입력받기

    # 코드가 숫자인지 확인
    try:
        decode = int(decode)
    except ValueError:
        print('코드는 숫자여야 합니다.')
        return  # 함수 종료

    # 입력받은 코드로 존재여부 확인
    message = f"SELECT COUNT(*) cnt FROM goods WHERE code={decode}"
    cursor.execute(message)
    cnt = cursor.fetchone()[0]

    if cnt == 0:
        print(decode, '코드 데이터는 미등록 삭제 데이터입니다\n')
    else:
        # 삭제 쿼리 실행
        msg = f"DELETE FROM goods WHERE code={decode}"
        cursor.execute(msg)
        CN.commit()
        print(decode, '코드데이터 삭제 처리 성공했습니다')

    # 전체 데이터 다시 출력 (삭제 후 확인)
    goodsSelectAll()


def goodsUpdate():  # 수정 갱신
    goodsSelectAll() 
    dcode = int(input('수정대상 코드 입력>> '))
    
    # 입력받은 코드로 존재여부 확인
    message = f"SELECT COUNT(*) cnt FROM goods WHERE code={dcode}"
    cursor.execute(message)
    cnt = cursor.fetchone()[0]
    
    if cnt == 0:
        print(dcode, '코드데이터는 미등록 갱신데이터입니다\n')
        return  # 존재하지 않으면 종료

    # 기존 코드가 아닌 다른 필드만 수정
    dname = input('수정이름 입력>> ')
    dsu = int(input('수량 입력>> '))  # 수량은 정수로 입력받음
    ddan = int(input('단가 입력>> '))  # 단가도 정수로 입력받음
    
    # 수정 쿼리
    msg = f"UPDATE goods SET name='{dname}', su={dsu}, dan={ddan} WHERE code={dcode}"
    cursor.execute(msg)
    CN.commit()
    
    print(dcode, '코드데이터 수정처리 성공했습니다 ')

    goodsUpdate() 


def goodsSearchName():
    print('이름데이터 like 조회 처리입니다 ')
    dname = input('이름조회>>> ')
    msg1 = f"SELECT * FROM goods WHERE name LIKE '%{dname}%'"
    cursor.execute(msg1)
    rows = cursor.fetchall()
    
    for r in rows:
        print(r)


# 메뉴 루프
while True:
    sel = int(input('1등록 2전체출력 3수정 4삭제 5이름조회 9종료>>> '))

    if sel == 1:
        goodsInsert()
    elif sel == 2:
        goodsSelectAll()
    elif sel == 3:
        goodsUpdate()
    elif sel == 4:
        goodsDelete()
    elif sel == 5:
        goodsSearchName()
    elif sel == 9:
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못된 선택입니다. 다시 시도하세요.")


goodsInsert()
# goodsSelectAll()
# goodsDelete()
# goodsSearchName()
# goodsUpdate()