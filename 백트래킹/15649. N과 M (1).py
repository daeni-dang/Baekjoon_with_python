import sys

n, m = map(int, sys.stdin.readline().split())

p = []
def f():
    if len(p) == m:
        sys.stdout.write(str(' '.join(map(str, p))) + '\n')
        return
    for i in range(1, n + 1):
        if i not in p:
            p.append(i)
            f()
            p.pop()
f()