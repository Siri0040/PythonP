A = [[1,1,1],
     [1,1,1]]

B = [[1,1],
     [1,1],
     [1,1]]

Res = [[0,0],
       [0,0]]

for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(A[0])):
            Res[i][j]=Res[i][j]+A[i][k]*B[k][j]

for r in Res:
    print(r)