def eratos(n):
    prime = [True] * (n + 1)
    for i in range(2, int(n ** 0.5) + 1):
        if prime[i]:
            for j in range(i * i, n + 1, i):
                prime[j] = False
    return prime
n = int(input())
for i in range(n):
    num = int(input())
    prime = eratos(num)
    prime[0] = False; prime[1] = False
    gold = []
    dif = 100000
    for j in range(num):
        if prime[j] and prime[num - j]:
            if abs(j - (num - j)) < dif:
                dif = abs(j - (num - j))
                gold.clear()
                gold = [j, num - j]
    print(gold[0], gold[1])