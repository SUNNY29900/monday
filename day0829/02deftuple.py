#02.deftuple.py


def my_hap(*args):
    print('*args타입', type(args))  #args 타입 'tuple'
    hap = 0 
    for num in args:
        hap=hap+num
    return hap 


# data=my_hap(6,11,24,7,3,21, 9, 45)
# print('데이터 결과', data)
# print('데이터 결과', my_hap(6,11,24,7,3,21, 9, 45)
 
mylist=[6,11,24,7]        #수정 o, 쉽게 데이터 추가
mytuple=(5,11,24,7)       #수정 x, 쉽게 데이터 추가

mylist[1]=54
print(mylist)

# mytuple[1] = 94 #에러 수정X
# print(mytuple)


print()
print('- ' * 50)



