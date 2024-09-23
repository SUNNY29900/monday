#05tuple.py

#튜플() 표시
#튜플은 리스트 비슷, 수정불가

pos=('홍대', 126.723, 37.081, '홍대', 290.345, 126.159)

#튜플 for 반복문으로 출력
for k in range(len(pos)):
      print(pos[k], end='\t')

print()  
print('-'*50)
print()

for i, v in enumerate(pos):
      print(i, ';', v )

print()