#13gugudan.py

data=input('구구단 입력>>>')
dan=int(data)
for k in range(1,10,1):
    print(dan, '*', k,'=', (dan*k))    #문자를 내가 입력한 숫자만큼 반복하는 것 의미

print()

'''
파이쎈 화면모니터 출력 print('안내문' 값)
파이쎈 키보드자판 입력 input('안내문')
파이쎈 키보드입력데이터 문자로 인식
int("1200") 숫자 120
'''

# a="12300"
# b="75"
# print(a+b)       #1230087

# c= int(a)+int(b)      #int정수= integer
# print(int(a)+int(b))  #int정수= integer
# print(c)

#파이쎈 내장함수
#print(), int(), round(), str(), sum()
