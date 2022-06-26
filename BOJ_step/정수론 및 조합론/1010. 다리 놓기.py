import sys
import math

n = int(sys.stdin.readline())
for i in range(n):
    n, m = map(int, sys.stdin.readline().split())
    sys.stdout.write(str(math.factorial(m) // (math.factorial(m - n) * math.factorial(n))) + '\n')