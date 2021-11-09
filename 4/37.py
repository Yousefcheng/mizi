def fun(choose):
    def pinfang(n):
        print(n**2)
    def lifang(n):
        print(n**3)
    if choose==2:
        return pinfang
    else:
        return lifang

n=int(input())
f1=fun(2)
f2=fun(3)
f1(n)
f2(n)