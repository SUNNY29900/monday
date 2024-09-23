#06testround.py

#변수 선언 및 초기화 
a, b, ret = 9, 4, 0
mok=34.5637

#실수 포맷팅 
print(mok)          #34.5637
print('%d'%(mok))  # 실수이지만 정수 34출력
print('%f'%(mok))  # %f는 자릿수 지정안하면 6자릿수까지 출력
print('%.2f'%(mok))  # %f는 자릿수 지정
print(round(mok,2))   #내장함수 round(값, 2)/ mok값을 소수점 이하 2자리 반올림


# 내장함수
# print(), int(), type(), input('안내문'), str() sum()
# round(데이터, 실수자릿수2)
# %자릿수 d정수 %자릿수 f실수
# 원하는 영역 블럭 선택후 ctrl +/슬래시
# 곱하기 연산처리

#문자열 포맷팅
ret=a*b

# print(변수, '문자', ~~), 나열식
print(a, '*', b, '=', ret)

# print('%d정수 %s문자열 %f실수 %c문자' %())
print('%d * %d= %d' %(a,b,ret))

# print('{}*{}={}'.format(a,b,ret))
print('{}*{}={}'.format(a,b,ret))

# print(f'{변수 및 값}')
print(f'{a}*{b}={ret}')

print()

