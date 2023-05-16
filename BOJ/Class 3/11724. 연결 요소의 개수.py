import sys
input = sys.stdin.readline

N, M = map(int, input().split())

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    a = find(x)
    b = find(y)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

parent = [i for i in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    union(u, v)

answer = set()
for i in parent[1:]:
    answer.add(find(i))
print(len(answer))