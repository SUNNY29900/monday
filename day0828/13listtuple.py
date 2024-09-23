#13listtuple.py

#리스트list 순서 유지, 중복허용
#튜플tuple 순서 유지, 중복허용
mylist=['kim', 78, True, 78, 3.1415,'kim']
mytuple=('lee', 78, False, 54, 3.1415,'lee')

mylist[1]=1200 #리스트변경가능      
mytuple[1]=1200 #튜플변경가능x

print(mylist)
print(mytuple)


print()
