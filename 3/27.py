'''
    
'''
raw=int(input())

matrix=[]
for i in range(raw):
    raw=input().split()
    raw=[eval(i) for i in raw]
    matrix.append(raw)

matrix[::] = [[row[i] for row in matrix] for i in range(len(matrix[0]))][::-1]

# print(matrix)

for r in matrix:
    for c in r:
        print(c,end=' ')
    print()