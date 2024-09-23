#06comprehension.py

print()
print()

mylist=[ a**2 for a in range(1, 11, 1)]
print(mylist)
print()

mytuple=(pow(b,2) for b in range(1, 11, 1))
print(mytuple)     # 리스트  coprehension적용은 튜츨제외
print()

myset={c**2 for c in range(1, 11, 1)}
print(myset)
print()