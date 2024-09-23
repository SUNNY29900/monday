#02testlist.py


data=[#4행*???행

       [71,72,73,70],
       [25,26,27,28],
       [39,10,11,12]

    ]


for k in range(len(data)): #4행
     for b in range (len(data[k])):  #열갯수
         print(data[k][b], end='\t')
     print()



#힌트 중첩for 반복문 권장, while반복문 비권장
#range(len()) 적절 이용하면 편해 
# for k in data:
#     print(k, end='')


    # 참조for a in range(0,3,1): #3행* 열갯수 고정일때  
    #  for b in range(0,4,1):
    #      print(data[a][b], end='\t')
    #  print()

#     print()
# print('-'*50)


# 1   2   3   4
# 5   6   7   8
# 9   10  11  12



