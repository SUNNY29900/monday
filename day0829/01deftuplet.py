# 01deftuple.py

def data_hap(x,y,z,a,b,c):
    #hap = 0 생략가능함
    hap = x+y+z+a+b+c
    return hap


def my_hap(*args):
    print('*args타입', type(args)) #*args타입 'tuple'
    hap = 0 
    for num in args:
        hap = hap + num
    return hap 


data = my_hap(6,11,24,7,3,21) 
print('데이터 결과 ', data)
print('데이터 결과 ', my_hap(6,11,24,7,3,21))
print()
print('- ' * 50)


total = data_hap(6,11,24,7,3,21)  
print('계산처리 합계 ', total)
print('계산처리 합계 ', data_hap(6,11,24,7,3,21))



'''
#id, type 함수 확인
def data_hap(x,y,z):
    #숫자합계구해서 리턴처리
    print('x id' , id(x)) #140727968479832 데이터를 기억하는 번지
    print('y id' , id(y)) #140727968479928 데이터를 기억하는 번지
    print('z id' , id(z)) #140727968480312 데이터를 기억하는 번지
    print('x타입' , type(x))
    print('y타입' , type(y))
    print('z타입' , type(z))

data_hap(6,9,21)
'''


print()



print()