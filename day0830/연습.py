
def gugudan(a):
    if a >=1 and a <= 9:
        for i in range(1,10):
            print(a,"*",i,"=", a*i,"")

    else:
        print("단은 1~9까지 입력해주세요")

d = int(input("단 : "))
gugudan(a)
