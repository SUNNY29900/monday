#06re.py

import re

#번째 정규식 예제
# #msg 변수에 새로운 내용 원래내용 덮어씌우는 재할당
msg= 'my best %#@& 245 오렌지 is (_^&^.^ 수박 cherry as tea'

result1=re. findall('[\w]+', msg)    #+붙이며 word로 나옴/ #비권장 
result2=re. findall('[\w]+', msg)
result3=re. findall('[a-zA-Z0-9가-힝]+', msg)
result4=re. findall('[^a-zA-Z0-9가-힝]+', msg)
print(result1); print()
print(result2); print()
print(result3); print()
print(result4); print()


print()
