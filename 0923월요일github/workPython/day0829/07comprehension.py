# 07comprehension.py [ 연산 if/else  for~~ ]

message=['spam', 'ham', 'spam', 'ham', 'spam', 'spam','spam']

# 문제1   for반복 ~ if제어
# spam출력 , 갯수출력 
message_cnt = 0
for k in message:
    if k=='spam':
        print(k, end=' ')
        message_cnt = message_cnt + 1
        #대입연산 message_cnt += 1 


print()
print('갯수 ',  message.count('spam') )
print('갯수 ', message_cnt )






# 문제2 [ 만앞 for~~~ if 조건만족 ] comprehension처리
# 방법1 temp_list= [ k for k in message  if 'spam' in k ]
# temp_list= [ k for k in message  if k=='spam' ]
# print(temp_list)











print()