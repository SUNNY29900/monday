#07rjust.py

for x in range(1,6,1):
    pass
    # print(f'{x}*{x}={x*x}')
    print(x, '*',x, '=', (x*x))

print()
for x in range(1,6,1):
    print(x, '*',x, '=', str(x*x).rjust(3))  #str 들어가는 순가 문자가 된 것


print()
for x in range(1,6,1):
    print(x, '*',x, '=', str(x*x).zfill(5))  





print()


