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
    
    # 코드 중복 검사
    check_query = f"SELECT COUNT(*) FROM sosi WHERE code = {dcode}"
    cursor.execute(check_query)
    cnt = cursor.fetchone()[0]
    
    if cnt != 0:
        print(f"{dcode}는 이미 등록된 코드입니다. 정확한 코드를 입력하세요.")
        return
    
    dname = input('이름 입력>> ')
    dtitle = input('제목 입력>> ')
    dsal = int(input('급여 입력>> '))
    
    # 데이터 삽입
    insert_query = f"""
    INSERT INTO sosi (code, name, title, sal, wdate, grade)
    VALUES ({dcode}, '{dname}', '{dtitle}', {dsal}, SYSDATE, 'C')
    """
    cursor.execute(insert_query)
    CN.commit()
    print(f"{dcode} 저장 성공했습니다.")
    time.sleep(1)

def sosiSelectAll():
    select_query = "SELECT * FROM sosi ORDER BY code"
    cursor.execute(select_query)
    rows = cursor.fetchall()
    
    print('%s\t %8s\t %10s\t  %4s\t %6s\t %s' % ('코드', '이름', '제목', '급여', '날짜', '등급'))
    for r in rows:
        print('%4d\t %10s\t %10s\t  %6.2f\t %s\t %s' % (r[0], r[1], r[2], r[3], r[4].strftime('%Y-%m-%d %H:%M:%S'), r[5]))
    
    print(f'전체 데이터 갯수: {len(rows)}')
    print('-' * 50)
    time.sleep(1)

def sosiSelectTitle():   #def sosiSelectTitle() 함수는 데이터베이스에서 제목을 기준으로 검색을 수행하고, 검색 결과를 출력하는 기능을 수행
    try:
        # 사용자로부터 제목 검색어 입력 받기
        search_title = input('검색할 제목의 일부 입력 (예: "%title%") >> ')
        
        # LIKE 검색 쿼리 작성
        select_query = """
        SELECT * FROM sosi
        WHERE title LIKE :title
        ORDER BY code
        """
        cursor.execute(select_query, {'title': search_title})
        rows = cursor.fetchall()
        
        if not rows:
            print("검색 결과가 없습니다.")
        else:
            print('%s\t %8s\t %10s\t  %4s\t %6s\t %s' % ('코드', '이름', '제목', '급여', '날짜', '등급'))
            for r in rows:
                print('%4d\t %10s\t %10s\t  %6.2f\t %s\t %s' % (r[0], r[1], r[2], r[3], r[4].strftime('%Y-%m-%d %H:%M:%S'), r[5]))
            
            print(f'검색 결과 갯수: {len(rows)}')
            print('-' * 50)
        time.sleep(1)
    except cx_Oracle.DatabaseError as e:
        print(f"데이터베이스 오류 발생: {e}")
    except Exception as e:
        print(f"오류 발생: {e}")























def sosiDelete():
    dcode = int(input('삭제할 코드 입력>> '))
    
    # 코드 존재 여부 확인
    check_query = f"SELECT COUNT(*) FROM sosi WHERE code = {dcode}"
    cursor.execute(check_query)
    cnt = cursor.fetchone()[0]
    
    if cnt == 0:
        print(f"{dcode}는 등록되지 않은 코드입니다.")
        return
    
    # 데이터 삭제
    delete_query = f"DELETE FROM sosi WHERE code = {dcode}"
    cursor.execute(delete_query)
    CN.commit()
    print(f"{dcode} 데이터가 삭제되었습니다.")
    time.sleep(1)
   
    #데이터 수정 
def sosiUpdate():
    try:
        dcode = int(input('수정대상 코드 입력>> '))

        # 코드 존재 여부 확인
        check_query = "SELECT COUNT(*) FROM sosi WHERE code = :code"
        cursor.execute(check_query, {'code': dcode})
        cnt = cursor.fetchone()[0]

        if cnt == 0:
            print(f"{dcode}는 등록되지 않은 코드입니다. 수정할 수 없습니다.\n")
            return

        # 필드 수정
        dtitle = input('수정제목 입력>> ')
        dsal = int(input('수정급여 입력>> '))
        dgrade = input('수정등급 입력>> ')  # 등급은 문자열로 입력받음

        # 데이터 수정
        update_query = """
        UPDATE sosi
        SET title = :title, sal = :sal, wdate = SYSDATE, grade = :grade
        WHERE code = :code
        """
        cursor.execute(update_query, {'title': dtitle, 'sal': dsal, 'grade': dgrade, 'code': dcode})
        CN.commit()
        print(f"{dcode} 코드 데이터가 수정되었습니다.")
    except cx_Oracle.DatabaseError as e:
        print(f"데이터베이스 오류 발생: {e}")
    except Exception as e:
        print(f"오류 발생: {e}")
    finally:
        time.sleep(1)



    # update_query = f"""
    # UPDATE sosi
    # SET title = '{dtitle', sal = dsal, wdate = SYSDATE, 'grade' = dgrade, 'code'=dcode
    # WHERE code = {dcode}
    # """
    # cursor.execute(update_query)
    # CN.commit()
    # print(f"{dcode} 코드 데이터가 수정되었습니다.")
    # time.sleep(1)


# 프로그램 실행 예시
# 프로그램 실행 예시
print("전체 데이터 조회:")
sosiSelectAll()
time.sleep(1)

print("데이터 삽입:")
sosiInsert()
print()

print("전체 데이터 조회:")
sosiSelectAll()
time.sleep(1)

print("데이터 삭제:")
sosiDelete()
print()





print("데이터 삽입:")
sosiUpdate()
print()

print("전체 데이터 조회:")
sosiSelectAll()