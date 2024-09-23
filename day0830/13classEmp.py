#13classEmp.py

#파이썬에서 클래스 이름만 명시
#클래스안에 있는 메소드매개인자(self)
#클래스안에 있는 메소드호출 ob=클래스()

class Emp:

    def insert(self):
        print('신규등록')
        print('딕트등록, 파일저장,  insert into 처리')
        print('insert into 처리\n')


    def delete(self):
        print('삭제처리')
        print('딕트del, delete, where 조건')

ob= Emp ()
ob.insert()
   #에러 delete()

print()
print('9월 2일 월요일 123')
print('9월 3일 화요일 456')
print('9월 4일 수요일 789')



print()