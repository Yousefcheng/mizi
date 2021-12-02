inp = [int(i) for i in input().split()]
n=inp[0]
m=inp[1]
g=[]
for s in range(n):
    temp=[int(i) for i in input().split()]
    g.append(temp)

dy=[1,-1,0,0]
dx=[0,0,1,-1]
def dfs(r,c):
    for i in range(4):
        x=r+dx[i]
        y=c+dy[i]
        if x<0 or x>=n or y<0 or y>=m:
            continue
        if g[x][y]==1:
            g[x][y]=0
            dfs(x,y)


ans=0
for i in range(n):
    for j in range(m):
        if g[i][j]==1:
            dfs(i,j)
            ans+=1

print(ans)