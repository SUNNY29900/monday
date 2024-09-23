#연습

#문자열
s1= 'Hello Python'
print(s1)
print()

#문자열 연결
head= "pathon"
tail="is fun"
print(head+tail)
print()

#문자열 곱하기
head*2
print(head*2)
print()
print("="*10)
print()

#문자열 인덱싱 
a="now is better than never"
first_char = a[0]
#first_char_upper = a[0].upper()
print(first_char)
print()           #결과값: n

#문자열 인덱싱 대문자까지
a="now is better than never"
first_char_upper = a[0].upper()
print(first_char_upper)
print()      #결과값 N

#문자열 인덱싱 2 : 4번째 문자열 알파벳
a="now is  better than never"
first_char = a[4]
print(first_char)
print()           #결과값: i


#문자열 인덱싱 3 :-1번째 문자열 알파벳
a="now is  better than never"
first_char = a[-1]
print(first_char)
print()           #결과값: r
#인덱스 -1은 마지막 문자의 인덱스의 맨 마지막 값의 문자인 r이 된다.

#문자열 인덱싱 4 :-2번째 문자열 알파벳
a="now is  better than never"
first_char = a[-2]
print(first_char)
print()        #결과값: e
 #인덱스 -2은 마지막 문자의 인덱스의 맨 마지막 앞 값의 문자인 e이 된다.


#문자열 슬라이싱   소문자
a="now is  better than never"
b = a[0:3]    #인덱스 0의 값은 문자 N, 콜론 왼쪽 범위시작 오른쪽 범위 끝 [4,6]->4,5 
print(b)
print()        #결과값: now


#문자열 슬라이싱  / 첫글자 대문자
a="now is  better than never"
b = a[0].upper() + a[1:3]    #인덱스 0의 값은 문자 N, 콜론 왼쪽 범위시작 오른쪽 범위 끝 [4,6]->4,5 
print(b)
print()   #결과값: Now

a="now is  better than never"
b = a[4:6]    #인덱스 0의 값은 문자 N, 콜론 왼쪽 범위시작 오른쪽 범위 끝 [4,6]->4,5 
print(b)
print()    #결과값: is


a="now is better than never"
b = a[19:]     #a[19:]는 문자열 a에서 인덱스 19부터 끝까지의 부분 문자열을 추출
print(b)
print()     #결과값:never


a="now is better than never"
b = a[:3]      #a[:3]는 문자열 a의 처음부터 인덱스 3까지의 부분 문자열을 추출
print(b)
print()            #결과값:now


a="now is better than never"
b = a[:]     #a[:]는 문자열 a의 전체를 슬라이스: a[:]는 start와 end를 생략한 형태로, 전체 문자열을 의미
print(b)
print()       #결과값:now is better than never

a="now is better than never"
b = a[7:-11]     #7 인덱스는 문자 'b', -11 인덱스는 문자열의 끝에서부터 11번째 문자를 의미: -11 인덱스는 't'
print(b)
print()           #결과값:better

#문자 개수 계산
a="Python"
print(a.count('p'))
print()      #결과값: 0

# 문자열 정의:

# a = "Pathon": 문자열 a는 'Pathon'입니다.
# 문자열 메서드 count():

# a.count('p'): 문자열 a에서 문자 'p'의 발생 횟수를 셉니다.
# 대소문자 구분:

# count() 메서드는 대소문자를 구분합니다. 즉, 'p'와 'P'는 서로 다른 문자로 간주됩니다.
# 문자 'p'의 개수:

# 문자열 'Pathon'에는 'p'라는 문자가 포함되어 있지 않습니다.
# 대문자 'P'는 있지만 소문자 'p'는 없습니다.

#문자위치 확인
a="Python"
print(a.find('y'))    #문자의 위치 인덱스 출력
print()      #결과값: 1

a="Python"
print(a.find('p'))    #문자의 위치 인덱스 출력
print()      #결과값: -1   #문자가 없으면 -1출력

a="Python"
print(a.find('P'))    #문자의 위치 인덱스 출력
print()       #결과값:  0

a="Python"
print(a.index('y'))    
print()      #결과값: 1

# a.index('y'): 문자열 a에서 문자 'y'의 위치를 찾음.
# index() 메서드는 문자열 내에서 지정한 문자가 처음 나타나는 위치의 인덱스를 반환. 
# 만약 문자가 문자열 내에 없으면 ValueError를 발생시킴.
# 문자 'y'는 문자열의 인덱스 1에 위치


#문자삽입
b= ","
c=b.join('abcd')
print(c)
print()    #결과값: a,b,c,d


