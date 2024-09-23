import cx_Oracle

# 사용자 입력 받기
dcode = int(input('코드입력>>>'))
dtitle = input('제목입력>>>')

# SQL 쿼리 문자열 생성
msg1 = f"SELECT * FROM some_table WHERE code = {dcode}"
msg2 = f"SELECT * FROM some_table WHERE title LIKE '%{dtitle}%'"

# 데이터베이스 연결 정보 설정
config = {
    'dsn': '127.0.0.1:5121/xe',  # DSN (Data Source Name)
    'user': 'system',      # 사용자 이름
    'password': '1234'   # 비밀번호
}

# 데이터베이스 연결 및 커서 생성
try:
    CN = cx_Oracle.connect(**config)
    cursor = CN.cursor()

    # SQL 쿼리 실행
    cursor.execute(msg1)
    results1 = cursor.fetchall()
    print("Results for msg1:")
    for row in results1:
        print(row)

    cursor.execute(msg2)
    results2 = cursor.fetchall()
    print("Results for msg2:")
    for row in results2:
        print(row)

finally:
    # 자원 정리
    cursor.close()
    CN.close()