'''
    
'''
# class computer_area():
#     0 2 2 0
#     1 2 3 0

x11,y11,x21,y21=[int(i) for i in input().split()]
x12,y12,x22,y22=[int(i) for i in input().split()]

xl=max(x11,x12)
yl=min(y11,y12)
xr=min(x21,x22)
yr=max(y21,y22)

if xl<xr and yl<yr:
    res=(yr-yl)*(xr-xl)
else:
    print(0)