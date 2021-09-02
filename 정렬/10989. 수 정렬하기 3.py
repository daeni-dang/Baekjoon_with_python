import sys

count = [0] * 10001
n = int(sys.stdin.readline())
for i in range(n):
    num = int(sys.stdin.readline())
    count[num] += 1
for i in range(10001):
    if count[i] != 0:
        for j in range(count[i]):
            sys.stdout.write(str(i) + '\n')