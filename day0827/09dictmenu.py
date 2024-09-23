#09dictmenu.py
#예외처리 try:~~except: ~~생략
import time
import sys  #프로그램 종료 sys.exit()

menu=dict()
flag=True
num, su, sel=0,0,0
msg, info, message='안내문', '안내', '안내메'

while flag:
    pass
    num=int(input('1등록 2출력 3수정 4삭제 5조회 9종료>>>'))

    if num ==9:
        print('딕트처리를 종료합니다\n')
        pass
        flag=False
        sys.exit()

    elif num ==1: # 딕트등록 mysite[200키]='kakao'
         name=input('이름입력key>>>')
         price=input('가격입력value>>>')
         menu[name]=price
         print(name, '등록성공했습니다')

    elif num ==2:#딕트에 전체 출력 for 반복문 권장
         for i, k in enumerate (menu):
             print(i, k, '', menu[k])
         print()

    elif num ==3: #딕트편집처리 가격대상 value변경
         name=input('편집대상 키값 입력>>>')
         if menu.get(name)==None:
            print('편집대상 딕트가  key 없습니다')
         else:
            price=input('변경 가격 재입력 value>>>')
            menu[name]=price
            print(name, '가격수정편집 성공했습니다')
            
    elif num ==4:
       print('key조회 삭제 나중에 주석')
       name=input('삭제대상 키값 입력>>>')
       if menu.get(name)==None:
           print('삭제대상 딕트가 key없습니다')

       else:
             #딕트삭제 pop(key)
             menu.remove(name)
             print(name, '데이터 삭제 성공했습니다')

    elif num ==5: #한건만 -본인꺼
       name=input('조회검색 key 입력>>>')
       if menu.get(name)==None:
            print('데이터가 없습니다')
       else:
         print(name, ':', menu[[name]])
    else:
        pass
        print('처리번호를 잘못 입력하셨네요\n')

print('')   

# 사용자 정의 함수
# 클래스 
# 파일처리-파일 저장, 파일열기
# 예외처리
# crud추가 
# ㄴ신규등록 create(insert=add)
# ㄴread읽기 update수정 delate삭제

# mysite = dict() #100k : 네이버v  200k : 카카오v
# mysite[100]='naver'
# mysite[200]='kakao'
# mysite[300]='apple'
# for i, k in enumerate(mysite):
#       print(i, k,' ', mysite[k])


# #출력 item(), enumerate(mysite)
# #수정 100: 네이버   100: 에어콘
# #key조회

# mysite[100]=' 에어콘'
# print()

# for k, v in mysite.items():
#       print(k, '', v)

# print()
# print(mysite[200])  #에러발생mysite[210]
# print(mysite.get(210))  #에러대신 none출력

# for k, v in mysite.items():
#       print(k, '', v)

# print()
# #print(mysite[200])  #에러발생mysite[210]
# print(mysite.get(210))  #에러대신 none출력
# print(210 in  mysite)  #에러대신false출력

# print()
