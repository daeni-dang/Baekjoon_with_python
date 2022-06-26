import math
def eratos(m, n):
    prime = [True] * (n + 1)
    for i in range(2, int(math.sqrt(n)) + 1):
        if prime[i]:
            for j in range(i + i, n + 1, i):
                prime[j] = False
    if m == n and prime[1]:
        return [n]
    return [i for i in range(2, n + 1) if prime[i] == True]

m, n = map(int, input().split())
prime = eratos(m, n)
for i in prime:
    if i >= m:
        print(i)