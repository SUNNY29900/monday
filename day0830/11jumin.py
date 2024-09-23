#11jumin.py


#방법1
import re
jumin = '870924-1674938'
my=int(jumin[7])
if my ==1  or my ==3:
      pass
elif my==2  or my==4:
      pass
else:
      pass

gender = re. search ( '(-)(\d{1})' , jumin )
print(gender)    # gender = re. search ( '(-)(\d{1})' , jumin )

genderNum=int(gender.group(2))    #<re.Match object; span=(6, 8), match='-4'>
print(genderNum)

#방법2
if genderNum==1 or genderNum==3:
    print('남자')
elif genderNum==2 or genderNum==4:
        print('여자')
else: 
      print('성별표기 오류입니다')