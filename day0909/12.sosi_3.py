#12. sosi_3.py  완성

import os
import pandas as pd
import cx_Oracle
import time

# 데이터베이스 연결 설정
config = {
    'user': 'system',
    'password': '1234',
    'dsn': '127.0.0.1:1521/xe'
}

# 데이터베이스 연결
CN = cx_Oracle.connect(**config)
cursor = CN.cursor()

def sosiInsert():
    dcode = int(input('코드 입력>> '))
    message = f"SELECT COUNT(*) FROM sosi WHERE code = {dcode}"
    cursor.execute(message)
    cnt = cursor.fetchone()[0]
    if cnt != 0:
        print(dcode, '코드데이터는 이미 등록된 코드입니다.')
        print('정확한 코드를 입력하세요.')
        return
    else:
        dname = input('이름 입력>> ')
        dtitle = input('제목 입력>> ')
        dsal = int(input('급여 입력>> '))
        msg = f"INSERT INTO sosi (code, name, title, sal, wdate, grade) VALUES ({dcode}, '{dname}', '{dtitle}', {dsal}, SYSDATE, 'C')"
        cursor.execute(msg)
        CN.commit()
        print(dcode, '저장 성공했습니다.')
        time.sleep(1)

def sosiSelectAll():
    msg = "SELECT * FROM sosi ORDER BY code"
    cursor.execute(msg)
    rows = cursor.fetchall()
    print('%s\t %8s\t %10s\t  %4s\t %6s\t %s' % ('코드', '이름', '제목', '급여', '날짜', '등급'))
    for r in rows:
        print('%4d\t %10s\t %10s\t  %4d\t %6s\t %s' % r)
    print('전체 데이터 갯수:', len(rows))
    print('-' * 50)
    time.sleep(1)

def sosiSelectTitle():
    try:
        search_title = input('검색할 제목의 일부 입력 (예: "%title%") >> ')
        select_query = "SELECT * FROM sosi WHERE title LIKE :title ORDER BY code"
        cursor.execute(select_query, {'title': search_title})
        rows = cursor.fetchall()
        
        if not rows:
            print("검색 결과가 없습니다.")
        else:
            print('%s\t %8s\t %10s\t  %4s\t %6s\t %s' % ('코드', '이름', '제목', '급여', '날짜', '등급'))
            for r in rows:
                print('%4d\t %10s\t %10s\t  %4d\t %6s\t %s' % r)
            print(f'검색 결과 갯수: {len(rows)}')
            print('-' * 50)
        time.sleep(1)
    except cx_Oracle.DatabaseError as e:
        print(f"데이터베이스 오류 발생: {e}")
    except Exception as e:
        print(f"오류 발생: {e}")

def sosiDelete():
    sosiSelectAll()
    print('삭제할 코드 입력>> ')
    dcode = int(input('삭제할 코드 입력>> '))
    message = "SELECT COUNT(*) FROM sosi WHERE code = {dcode}"
    cursor.execute(message)
    cnt = cursor.fetchone()[0]
    if cnt == 0:
        print(dcode, '코드데이터는 미등록된 데이터입니다.')
    else:
        msg = f"DELETE FROM sosi WHERE code = {dcode}"
        cursor.execute(msg)
        CN.commit()
        print(dcode, '데이터 삭제 성공했습니다.')
    sosiSelectAll()

def sosiUpdate():
    sosiSelectAll()
    dcode = int(input('수정할 코드 입력>> '))
    message = f"SELECT COUNT(*) FROM sosi WHERE code = {dcode}"
    cursor.execute(message)
    cnt = cursor.fetchone()[0]
    if cnt == 0:
        print(dcode, '코드데이터는 미등록된 데이터입니다.')
    else:
        dtitle = input('수정제목 입력>> ')
        dsal = int(input('수정급여 입력>> '))
        dgrade = input('수정등급 입력>> ')
        msg = f"UPDATE sosi SET title = '{dtitle}', sal = {dsal}, wdate = SYSDATE, grade = '{dgrade}' WHERE code = {dcode}"
        cursor.execute(msg)
        CN.commit()
        print(dcode, '코드데이터 수정 성공했습니다.')
    sosiSelectAll()

def main():
    while True:
        print('1: 등록 2: 전체출력 3: 수정 4: 삭제 5: 제목조회 9: 종료')
        choice = input('선택하세요 >> ')
        
        if choice == '1':
            sosiInsert()
        elif choice == '2':
            sosiSelectAll()
        elif choice == '3':
            sosiUpdate()
        elif choice == '4':
            sosiDelete()
        elif choice == '5':
            sosiSelectTitle()
        elif choice == '9':
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 다시 선택해주세요.")
        
if __name__ == '__main__':
    main()