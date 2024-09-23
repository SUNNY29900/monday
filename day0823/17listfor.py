#17list.py
import time

mylist=['tea', 7] 
print(mylist)

mylist.append('파이썬')
print(mylist)

mylist.append(23)
print(mylist)

mylist.insert(23)
print(mylist)


mylist.insert(1, 'blue')
print(mylist)
print('-'*50)

#수정할때  수정하는 함수 없음
mylist[0]='kakao'
mylist[2]='94'
print(mylist)

# blue삭제 del mtlist[1], remove pop(위치)
del mylist[1]
print(mylist)

#에러 mylist.sort()
#주의사항 sort() 적용은 같은 타입만 가능
#for a in mylist
#    print(a, end='  ')

print()
print()

#잔액 나오기만들기