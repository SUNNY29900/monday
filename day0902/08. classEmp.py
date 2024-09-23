# 08 classEmp.py

class Emp:
    user_pwd='1234'    
    user_pwd='아이디'    
    # member 변수 = global variable = public variable
    
    def __init__(self, id, pwd) :
        self.user_pwd = id 
        self.user_pwd = pwd  

    def insert(self, nick, age):
        print('전역변수', self.user_id)
        print('전역변수', self.user_pwd)
        print('전달된 나이', age)
        print('insert into처리\n')

    def delete(self):
        print('삭제처리')
        print('딕트del, delete where 조건')
        
ob = Emp('sky','7788')
ob.insert(7)
ob.delete()

print()