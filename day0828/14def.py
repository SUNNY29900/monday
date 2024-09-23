#14def.py

import datetime
import time

'''
파이썬에서 함수 정의 시작 키워드 def  함수이름():
사용자정의 함수 매개인자  구구단 실습
사용장정의 함수 리턴값
사용자정의 함수 매개인자 +리턴값
'''

#함수정의 = 구현=기술 함수 =function=기능
def gugudan(writer, dan):
    print('구구단 저자 ', writer)
    for k in range (1,10):
        print(f'{dan}*{k}={dan*k}')
        time.sleep(0.3)


#myTotal함수기술 총점, 평균 출력  공격수 최진호, 수비수 최진호
def myTotal(kor, eng, mat):
    print('myTotal 함수영역')
    hap=kor+eng+mat
    avg=hap//3
    print('myTotal 총점=', hap)
    print('myTotal 평균=', avg)

print()


# 함수호출
if __name__=='__main__': #생략가능
     gugudan('lee', 7)
     kor=90
     eng=85
     mat=60
     myTotal(kor, eng, mat)
print()