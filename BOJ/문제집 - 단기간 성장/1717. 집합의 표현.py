import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

if __name__ == "__main__":
    n, m = map(int, input().split())
    parent = [i for i in range(n + 1)]
    for _ in range(m):
        o, a, b = map(int, input().split())
        if o == 0:
            union(a, b)
        else:
            if find(a) == find(b):
                print("YES")
            else: print("NO")