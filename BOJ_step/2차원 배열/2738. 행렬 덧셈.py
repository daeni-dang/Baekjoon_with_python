n, m = map(int, input().split())
A = []
B = []
C = []

for i in range(n):
    A.append(list(map(int, input().split())))
for i in range(n):
    B.append(list(map(int, input().split())))
for i in range(n):
    tmp = []
    for j in range(m):
        tmp.append(A[i][j] + B[i][j])
    C.append(tmp)

for i in range(n):
    for j in range(m):
        print(C[i][j], end=' ')
    print()