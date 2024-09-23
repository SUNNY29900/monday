#01 string.py

#a문자 숫자 섞여쓰면 에러, 따라서 str통해 사용
#str(), len()
x='blue'
y=1234
print(x+str(y))
print(f'{x}{y}')  #분리  문자는 문자대로, 숫자는 숫자대로
print(x,y)  #분리사이 공백표시, 문자 숫자
print('-' *50)

msg='sakbtb'
print('길이', len(msg))    
print('갯수', msg.count('b'))
#kb글자단어를 추출[시:끝+1]
my=msg[2:4]
print(my)
print(msg[2:4])

print()