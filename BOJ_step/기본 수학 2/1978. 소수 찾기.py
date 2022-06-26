import math
def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

n = int(input())
tmp = input()
num = 0
for i in range(n):
    if isPrime(int(tmp.split()[i])): num += 1
print(num)