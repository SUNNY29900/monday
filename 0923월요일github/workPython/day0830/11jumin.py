import re

jumin='870924-1674938'

my = int(jumin[7])
if my==1 or my==3:
    pass
elif my==2 or my==4:
    pass
else:
    pass 

gender = re.search('(-)(\d{1})', jumin)
print(gender) #~~ Object; span=(6, 8), match='-4'>

genderNum = int(gender.group(2))
print(genderNum)
if genderNum==1 or genderNum==3 :
    print('남자')
elif genderNum==2 or genderNum==4 :
    print('여자')
else:
    print('성별표기 오류입니다 ')















print()