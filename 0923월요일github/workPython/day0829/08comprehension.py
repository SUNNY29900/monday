# 08comprehension.py [ 연산 if/else  for~~ ]

message=['ham', 'spam', 'spam', 'ham', 'spam', 'ham','spam']
dummy = [ ]


# 문제 spam=0 ham=1 dummy = [1,1,0,1,0,1,0]
# message=['ham', 'spam', 'spam', 'ham', 'spam', 'ham','spam']
for k in message:
    if k=='spam':
        dummy.append(0)
    else:
        dummy.append(1)

print('반복~제어정석 ', dummy)

mydummy = [ 0 if k=='spam' else 1 for k in message ]
print('comprehension ', mydummy)








print()