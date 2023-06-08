import sys
input = sys.stdin.readline

def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y
    
def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

if __name__ == "__main__":
    n = int(input())
    m = int(input())
    graph = []
    for r in range(n):
        arr = list(map(int, input().split()))
        for i in range(n):
            if arr[i] == 1:
                graph.append([r + 1, i + 1])
    sch = list(map(int, input().split()))
    
    parent = [i for i in range(n + 1)]
    for x, y in graph:
        if find(x) != find(y):
            union(x, y)
    
    cur = find(sch[0])
    for i in range(1, m):
        if find(sch[i]) != cur:
            print("NO")
            break
    else:
        print("YES")