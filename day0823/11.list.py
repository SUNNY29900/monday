#11list.py

lista=[2,1,4,5,3]
print(lista)   

time.sleep(1)
lista.insert(2,9)   #2번째 위치에 추가
print(lista)

time.sleep(1)
lista.append(7)     #맨끝에 추가 append
print(lista)

time.sleep(1)
#lista.remove(8) 데이터값없으면 에러발생
lista.pop(3)
print(lista)

time.sleep(1)
lista.reverse()
print(lista)

#lista.sort()
#lista.sort()


