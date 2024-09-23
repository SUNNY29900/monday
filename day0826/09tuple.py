#09tuple.py

t = (30, 20, 10, 50, 63, 7, 7, 67, 65, 20, 30, 63)
print('갯수', t.count(10))
print('색인', t.index(50))

print(t)
print()

mylist=list(t)
mylist=list(mylist)
mylist.append(7)
mylist.insert
print(mylist)
print()
print(tuple(mylist))   #수정,삭제,추가 할 수 없음

#에러 t.append(7)
#에러 t.insert(2,63)
#에러 t. remove(20)
print()