# 04testlambda.py
# 람다식은 import 기술안함,  키워드 lambda기술

def mycal(su):
    return su*su


print('일반식', mycal(6))
my1 = lambda su : su*su
print('람다식', my1(6)) 
print('람다식', (lambda su : su*su)(6)) 
print()



def myAdd(x,y):
    return x+y

print('일반식', myAdd(11,9)) 
my2 = lambda x,y : x+y
print('람다식', my2(11,9)) 
print('람다식', (lambda x,y : x+y)(11,9)) 


print('- ' * 50)
print()
# 함수에서  계산처리후 if~else제어문  리턴값
def myCheck(su): 
    msg = '안내문'
    if su%2 == 0:
        msg = '짝수'
    else:
        msg = '홀수'
    return msg 


print('일반식', myCheck(7))
print('람다식', (lambda su: '짝수' if su%2==0 else '홀수')(7))
print()


# 문제 리스트 1 2 3 ~ 8 9 10 
data = list(range(1,11,1))  #출력[1, 2, 3 ~ 8, 9, 10]
print(data)    
my = list(map((lambda su : su*su),data))
print(my)

# 에러print('람다식', (lambda su : su*su)(data)) 
# 첫번째예제 성공 print('람다식', (lambda su : su*su)(6))
# my =  map((lambda su : su*su),data)
# print(my) #<map object at 0x00000269C8B95420>
# print(list(my)) #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]







print()