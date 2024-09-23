#remailcheck.py

import re

def email_check (email):
    pass
    #re.findall('^시작.[a-z]{2,}$끝,   )   -> re.findall('^.[a-z]{2,},   ) 패턴의 시작을 의미/ 아니야라는 의미 아님
    #re.findall('.[^a-z]{2,},   )      ->re.findall('.[^a-z]{2,},   )  여기에서 ^ 의미는 부정의 의미 

email_check("kim@gmail")        #.org   .kr    .com    .net
email_check("kim_gmail.net")    #포함여부
email_check("$^kim")            #첫 글자 특수문제 포함
email_check("kim@gmail.net")    #올바른 이메일입니다

