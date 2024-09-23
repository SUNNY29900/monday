# 05list.py
import time

# 숫자타입으로 된 가장 대표적인 리스트 
lotto = [34, 7, 19, 42, 6, 21]

for k in range(1,11,1):
    su = k**2
    print( su, end='\t')


print()
time.sleep(1)
for k in range(1,11,1):
    su = pow(k,2)
    print( su, end='\t')


print()
print()
print('- ' * 50)
time.sleep(1)
mylist = [ a**2  for a in range(1,6,1)]
print(mylist)
print()

# mytuple = ( b**2 for b in range(1,11,1))  
# print(mytuple) #리스트 comprehension적용은 튜플제외
# print()

myset = { c**2 for c in range(1,6,1)}
print(myset)
print()











print()