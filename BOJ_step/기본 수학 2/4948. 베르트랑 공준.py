def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

prime = []
for i in range(1, 246912):
    if is_prime(i):
        prime.append(i)
while True:
    n = int(input())
    if n == 0: break
    num = 0
    for i in prime:
        if n < i <= 2 * n:
            num += 1
    print(num)