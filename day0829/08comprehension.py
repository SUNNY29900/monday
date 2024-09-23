#08comprehension.py[연산 if/else   for~~]

print()
print()

message=['ham', 'ham','spam', 'ham','spam', 'ham' ]
#문제1 for 반복~ if 
#span출력, 갯수 몇 개인지 출력
for k in message:
    if k =='spam':
        print(k, end='')

print()
print()
temp_list=[k for k in message if k == 'spam' in k ]
print(temp_list)


print()
dummy=[]
#문제3   spam=[0]   ham=[1] dummy=[1,1,0,1,0,1,0]
# massage=['ham','ham' 'spam','ham', 'spam', 'ham','spam']
for k in message:
    if k =='spam':
        dummy.append(0)  #append는 내장함수 따라서 ()써야함
    else:
        dummy.append(1)

print('반복~제어정석', dummy)


mydummy=[ 0 if k=='spam' else 1 for k in message ]
print('comprehension', mydummy)
