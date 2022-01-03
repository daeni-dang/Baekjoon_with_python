import sys

n, m = map(int, sys.stdin.readline().split())

p = []

def f():
    if len(p) == m:
        sys.stdout.write(' '.join(map(str, p)) + '\n')
        return
    for i in range(1, n + 1):
        p.append(i)
        f()
        p.pop()
f()