n = int(input())

d = [0] * (n + 1)

def fibo_recur(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fibo_recur(x - 1) + fibo_recur(x - 2)
    return d[x]

def fibo_iter():
    d = [0] * (n + 1)
    d[1] = 1
    d[2] = 1
    for i in range(3, n + 1):
        d[i] = d[i - 1] + d[i - 2]
    return d[i]

print(fibo_recur(n))
print(fibo_iter(n))