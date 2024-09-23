#02test.py

mylist=[  ] #리스트 선언
mydict={} #딕트 선언

mylist. append('lee')
mylist. append('90')
mylist. append('85')
mylist. append('True')
mylist.insert(1, '빅데이터')
#문제 85데이터 삭제 remove(), pop(), del[]
mylist.remove(85)
for k in mylist:   #비권장
      print(k, end='\t')
print()


mydict[500]= '차박'
mydict[700]= '등산'
mydict[300]= '여행'
for k,v in mydict.items():
    print(k,':', v)

print()
for i, k in enumerate(mydict):
    print((i+1), '', k, mydict[k])

#리스트갯수 count(데이터), len())
cnt=mylist.count(90)
print('리스트갯수', mylist.count(90))