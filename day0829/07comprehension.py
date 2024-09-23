#07comprehension.py[연산 if/else   for~~]

print()
print()

message=['ham', 'ham','spam', 'ham','spam', 'ham' ]
#문제1 for 반복~ if 
#span출력, 갯수 몇 개인지 출력
message_cnt=0
for k in message:
    if k =='spam':
        print(k, end='')
       #정석 message_cnt=message_cnt+1
        message_cnt+=1   #대입연산


print()
print('갯수', message.count('spam'))
print('갯수', message_cnt)
#문제2 [앞(만족) if조건 else for~~~~]comprehension   for처리
#문제2 [앞 if조건 else 뒤(불만족)for]comprehension   for처리
# 방법1 temp_list=[k for k in message if k == 'spam']
# 방법2 temp_list=[k for k in message if k == 'spam' in k ]

print()


