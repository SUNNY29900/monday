#10testlamda.py


# 람다-익명의 함수 = 함수이름이 없어요
# 람다식은 import없습니다. 
# 람다식은 lambda 키워드 기술

def mysu(num): 
    value=3*num+5
    return value 

data=int(input('숫자입력>>>'))
print('일반식', mysu(data))
print('람다식', (lambda num:3*num+5)(data))







print()

