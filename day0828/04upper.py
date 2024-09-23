#04upper.py
#교재86~90페이지 참고

msg='bstzpchEReey'
print(msg.upper())  #대문자
print(msg.lower())  #소문자
print()
print('k=', msg.find('k'))   #k=3위치
print('t=', msg.index('t'))   #t=2위치


print()


print('.'*50)


msg='bstzpchEReey'
print(msg.upper())  #대문자
print(msg.lower())  #소문자
print()
print('z=', msg.find('z'))   #z=3위치
print('z=', msg.index('t'))   #z=-1
#인덱스 없으면 에러
pos= msg.find('z') 
if pos==-1:
     pass
else:
     pass
     #있으면 출력을 하거나 조작, 연산처리
     print('원하는 키워드가 없습니다')
print()


print('.'*50)


