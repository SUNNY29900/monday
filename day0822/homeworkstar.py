#homeworkstar.py문서
#100페이지 while 반복문 사용금지

#조건 중복 for반복문
#처리 지역변수, 특정변수 필요없음
#반복문 대표변수  x,y   i,j  a,b
#for a in range(1, 11, 1):
#    for b in range(1,11,1):
#        pass 


# ☆ 윈도우+. 이모지 사용

#행 수 설정


for a in range(1, 6, 1):
        print(a)                

print()

"""
☆
☆☆
☆☆☆
☆☆☆☆
☆☆☆☆☆
"""

# 행 수 설정
n = 5
#행 수만큼 반복
for i in range(1, n+1):
# 각 행에 i개의 별표 출력
    print('☆' * i)

    print()


for a in range(1, 6, 1): #행=가로=row처리후 라인개행
        for a in range(1, a, 1):
                print(' ★ ', end = '' )
                print('😍', end='')
        print() 

for a in range(1, 6, 1): #행=가로=row처리후 라인개행
        for a in range(1, a, 1):
                print(' ★ ', end = '' )
                print('😍')
        print() 

for a in range(1, 6, 1): #행=가로=row처리후 라인개행
        for a in range(1, a, 1):
                print(' ★ ', end = '' )
        print() 

for a in range(1, 6, 1): #행=가로=row처리후 라인개행
        for a in range(1, a, 1):
                print(' 😍 ', end = '' )
        print() 


for a in range(1, 7, 1): #행=가로=row처리후 라인개행
        for a in range(1, a, 1):
                print(' 😍 ', end = '' )
        print() 




for a in range(1, 7, 1): #a=1일때 행=가로=row처리후 라인개행
        for b in range(0, a, 1):
                print(' 😍 ', end = '' )
        print() 