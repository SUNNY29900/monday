#06testor.py

'''
if 조건 :
만족문장기술
elif 조건2 :
    조건2 만족 문장기술 
elif 조건3 :
조건3 만족 문장기술 
else:
불만족문장기술

'''
#선언=declare
kor, eng, hap=0,0,0
avg=0.0
message= '안내문' 

#처리연산, if, 반복
kor=90
eng=95
hap=kor+eng
avg=hap/2

#문제해결1) 평군 70점부터 축합격, 0~69재시험
if avg >=70 : 
    message = '축합격'
else : 
    message = '재시험'     


#잘못된 처리) 평균 100~90 A, 89~80 B, 79~70 C, 69~60 D, 59~0 F
if avg>=90:
   grade='A'
if avg >= 80:
   grade='B'
if avg >= 70:
   grade='C'
if avg>= 60:
   grade='D'
else:
   grade='F'  


#문법에러, 처리상 버그=에러
#출력
print('02testif. py문서')
print('국어', kor)
print('영어', eng)
print('합계', hap)
print('평균', avg)
print('학점', grade)
print('결과', message)
print('-' *50)
print()