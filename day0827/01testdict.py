#01test.py

mylist=[  ] #리스트 선언
mydict={} #딕트 선언

mydict[500]= '차박'
mydict[700]= '등산'
mydict[300]= '여행'
for k,v in mydict.items():
    print(k,':', v)

print()
for i, k in enumerate(mydict):
    print((i+1), '', k, mydict[k])