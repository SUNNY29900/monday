#03listsearch.py

data=[7,8,9,1,2]
ss=int(input('데이터 찾기>>>'))
if ss in data : 
    print(ss, '검색성공 ok')
    # #print('결과',  ss in data)
else:
    print('결과',  ss in data)
    # #print(ss, '검색실패 failed')


# 데이터있으면 성공메시지 데이터 출력
# 데이터없으면 실패메시지 데이터 출력
# 참고for 대표 변수 in range(5): 
# list에서 데이터 찾기 할때 in 키워드 사용
