#testkor.py

#선언부분=변수데이터 초기화 = declare

title='데이터 점수'
name='길동'
kor=90
eng=85
hap=0
avg=0.0

#로직 =연산
hap=kor+eng
avg=hap/2

#처리결과 출력 print('안내문', '데이터')  f-string 포맷팅
#print(f'{title}- 이름:{name}, 합계:{hap}, 평균:{avg:.2f}')  ->avg 변수를 소수점 이하 2자리까지 포맷팅하여 출력
print()
print(f'{title} - 이름: {name}, 합계: {hap}, 평균: {avg}')
#출력값 데이터 점수 - 이름: 길동, 합계: 175, 평균: 87.5





