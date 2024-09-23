# 16sortinsert.py
print()

a=[4,7,5,1,2] 
for i in range(4):  #기준 처음기준
    for j in range(i,5): #비교대상
        if a[i]>a[j] :
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
    print(a)  #작은바퀴회전후 출력

# [1, 7, 5, 4, 2] 0회 
# [1, 2, 7, 5, 4] 1회 
# [1, 2, 4, 7, 5] 2회
# [1, 2, 4, 5, 7] 3회
