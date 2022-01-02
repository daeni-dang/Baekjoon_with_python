import sys

n, m = map(int, sys.stdin.readline().split())

p = []

def f(start):
    if len(p) == m:
        sys.stdout.write(' '.join(map(str, p)) + '\n')
        return
    for i in range(start, n + 1):
        if i not in p:
            p.append(i)
            f(i + 1)
            p.pop()
f(1)