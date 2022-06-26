import sys
def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)
x, y = map(int, sys.stdin.readline().split())
gcdNum = gcd(x, y)
sys.stdout.write(str(gcdNum) + '\n')
sys.stdout.write(str(int(x * y / gcdNum)) + '\n')