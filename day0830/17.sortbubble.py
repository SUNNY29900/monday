#14sort.py

print()

a=[4,7,5,1,2];
for i in range(4):   #기준 처음 기준
   for j in range (i,5):  #비교대상
      
      if a [i]>a[j]:
         temp=a[i]
         a[i]=a[j]
         a[j]=temp
print(a)   #작은바퀴회전 후 출력


#[1,7,5,4,2]  0회
