from scipy.sparse import csr_matrix

row=[int(i) for i in input().split()]
col=[int(i) for i in input().split()]
data=[int(i) for i in input().split()]
num=max(row)+1
mat = csr_matrix((data,(row,col)),shape=(num,num))
# print(mat)
print(mat.todense())