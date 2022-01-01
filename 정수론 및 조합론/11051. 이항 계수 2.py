import sys
import math

n, k = map(int, sys.stdin.readline().split())
sys.stdout.write(str(math.factorial(n) // (math.factorial(n - k) * math.factorial(k)) % 10007) + '\n')
