#16defreturn.py

def book():
   title='몽블랑'  #지역변수 =local variable= 휘발성
   return title 

def pay():
   m=7800  #지역변수 =local variable= 휘발성
   return m 


#리턴닶 x 없는 호출해서 출력하면 None
def blue():
   color='dark'

def main():
   print("main 함수")  
   print("책제목", book())
   print("책가격", pay())
   print("블 루", blue())   #none 필드/ pass 필드

# #함수 단독기술해서 호출
#    main()

#     #함수호출
#     #if__name__== '__main__': 생략가능

print()
print()