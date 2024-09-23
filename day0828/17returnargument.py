#17returnargument.py

def book():   #매개인자x, 리턴값0
   title='몽블랑'  
   return title 

def pay():     #매개인자x, 리턴값0
   m=7800  
   return m 

def myCal(x,y,z):   #매개인자x, 리턴값0
   total= x+y+z
   avg=total//3
   #3개 데이터를 받아서 계산연산 처리후 최종값 리턴
   return avg

# myCal 함수 호출   90  85  64
# myCal 함수 리턴값이 있으면 변수= 함수이름
# myCal 함수 리턴값이 있으면 print(함수이름())
data=myCal(90,85,64)
print('mycal함수결과', data)
print('mycal함수결과', myCal(90,85,64))


# def gugudan(name, dan):    #매개인자0.리턴값x
#    pass
# #name 출력 반복문 dan 출력

# def blue():       #매개인자x, 리턴값x
#    color='dark'

# def main():
    

#    main()

   
print()
print()
