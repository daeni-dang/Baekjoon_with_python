import sys
n, m = map(int, sys.stdin.readline().split())
s = set()
check = []
answer = 0
for _ in range(n):
    s.add(sys.stdin.readline().strip())
for i in range(m):
    cur = sys.stdin.readline().strip()
    if cur in s:
        answer += 1
sys.stdout.write(str(answer))