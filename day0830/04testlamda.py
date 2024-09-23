# 01testlambda.py
# 람다식은 import 기술안함, 키워드 lambda 기술

def mycal(su):
    return  su*su

# def mycal():
#     passcal= cal
#     return 3*su+8


print('일반식', mycal(6))
my1 = lambda su:  su*su
print('람다식', my1(6))       
print('람다식', (lambda su: su*su )(6))
print()

def myAdd(x,y):
    return  x+y

print('일반식', myAdd(11,9))
my2 = lambda x, y:x+y
print('람다식', my2(11,9))
print('람다식', (lambda x,y:  x+y )(11,9))
print()

print('-'*50)
print()
#함수에서 계산 처리후 if ~~else제어문 리턴값
def myCheck(su):
    #pass if ~else  짝수/홀수 
    msg='안내문'
    if su%2== 0:
        msg= '짝수'
    else:
        msg= '홀수'
    return msg

print('일반식', myCheck(7))
print('람다식', (lambda su:'짝수' if su%2==0 else '홀수')(7))
                     #수식
print()



#문제 리스트 1 2 3 ~8 9 10
data=list(range(1,11,1)) #출력[1,2,3~8,9,10]
print(data)
my=list(map((lambda su: su*su), data))  
print(my)

#에러 print('람다식', (lambda su : su*su)(data))
#첫번째 예제 성공 print ('람다식', (lambda su : su*su)(6))
#my=map((lambda su : su*su))







#문제 리스트 1~10까지(1 2 3 ~8,9,10) 출력    for. while 반복문 사용금지 
# data=range(1,11,10)  #range(1, 11, 10)출력
# print(data)





data=list(range(1,11,1))    #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]출력
print(data)    #1*1   2*2   3*3  4*3  ~  8*8  9*9 10*10
print(data*2)   #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]출력  
# print('람다식', lambda su :su*su(data))  -> 에러 
# 첫번째 예제 성공 print('람다식', (lambda su: su*su )(data))

my =map((lambda su: su*su ),data)
print(my)   #<map object at 0x00000160320AE5C0>
# print(list(my))   #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]








print()


