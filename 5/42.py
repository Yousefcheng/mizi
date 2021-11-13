class get_result:
    def __init__(self) -> None:
        pass
    def jiecheng(self,n):
        if n==1:
            return 1
        else:
            return self.jiecheng(n-1)*n


num=int(input())
temp=get_result()
result=temp.jiecheng(num)

print(str(result))