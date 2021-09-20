import sys
def gcd(x, y):
    if x % y == 0:
        return y
    else:
        return gcd(y, x % y)
def lcm(x, y):
    return x * y / gcd(x, y)
n = int(sys.stdin.readline())
for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    sys.stdout.write(str(int(lcm(x, y))) + '\n')