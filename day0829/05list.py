#05list.py

lotto=[34,7,19,42,6,21]
for k in range (1,11,1):
    su=k**2
    print(su, end='\t')


print()

for k in range(1, 11, 1):
    su=pow(k,2)
    print(su, end='\t')

print()


for k in range(1,11,1):
    su=pow(k,2)
    print(su,end='\t')

print()
print()
print('.'*50)
time.sleep(1)
mylist=[ a**2 for a in range(1, 6, 1)]
print(mylist)
print()

mytuple=(pow(b,2) for b in range(1, 11, 1))
print(mytuple)     # 리스트  coprehension적용은 튜츨제외
print()

myset={c**2 for c in range(1, 6, 1)}
print(myset)
print()