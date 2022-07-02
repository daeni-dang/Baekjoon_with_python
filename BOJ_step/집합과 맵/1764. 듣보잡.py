import sys

n, m = map(int, input().split())
deutdo = set()
bodo = set()
for i in range(n):
    deutdo.add(sys.stdin.readline().strip())
for i in range(m):
    bodo.add(sys.stdin.readline().strip())

deutbo = list(deutdo & bodo)
print(len(deutbo))
deutbo.sort()
[sys.stdout.write(i + "\n") for i in deutbo]