A = [[1,2,3,4],
     [10,11,12,5],
     [9,8,7,6]]

T=0
B=len(A)-1
L=0
R=len(A[0])-1
dir=0
while L<=R and T<=B:
    if dir==0:
        for i in range(L,R+1):
            print A[T][i]
        T=T+1
        dir=1
    elif dir==1:
        for i in range(T,B+1):
            print A[i][R]
        R=R-1
        dir=2
    elif dir==2:
        for i in range(R,L-1,-1):
            print A[B][i]
        B=B-1
        dir=3
    elif dir==3:
        for i in range(B,T-1,-1):
            print A[i][L]
        L=L+1
        dir=0

