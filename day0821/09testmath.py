# 09 testmath.py
import math


a=25
b=5
print(math.sqrt(a))  #5.0    실수형태    #math.sqrt(a)는 숫자 a의 제곱근을 계산하는 함수
print(math.pow(b,2)) #25.0   실수형태
print(math.pow(b,3)) #125.0  실수형태

# square +root = sqrt  보통 x^2 또는 x ** 2
# pow=power*2
# math라이브러리 결과값이 실수형태
# 내장함수 print(). round(숫자, 자릿수), int(), type()
# 함수사용시 꼭 추가 키워드, import라이브러리
#mok=934.5637
#print(round(mok,2))   #내장함수 round(값, 2) 934.56


#math.sqrt(a):

# 설명: math.sqrt() 함수는 a의 제곱근을 계산합니다. 제곱근은 어떤 수를 제곱했을 때 원래 숫자가 되는 수를 말합니다.
# 입력: a의 값이 25이므로, math.sqrt(25)는 25의 제곱근을 계산합니다.
# 출력: 5.0. 즉, 25의 제곱근은 5입니다 (5 * 5 = 25).