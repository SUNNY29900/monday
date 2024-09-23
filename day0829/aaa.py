# 문제2  나이입력 범위 20~70사이
#          조건 20미만 청소년 1~19  20~30청년  31~65 중년  66이상 노년
if 'age' <20:
    age_catefory='청소년'

elif 20<= 'age'<=30:
    age_catefory='청년'

elif 31<= 'age'<=65:
    age_catefory='중년'

else:
    age_category = '노년'