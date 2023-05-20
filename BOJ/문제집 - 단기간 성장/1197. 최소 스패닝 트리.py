import sys
input = sys.stdin.readline

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, x, y):
    x = find(parent, x)
    y = find(parent, y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

if __name__ == "__main__":
    V, E = map(int, input().split())
    graph = []
    # 부모 자기 자신으로 초기화
    parent = [i for i in range(V + 1)]
    for _ in range(E):
        A, B, C = map(int, input().split())
        graph.append([C, A, B])
    
    # 간선의 가중치로 초기화
    graph.sort()
    
    answer = 0
    
    for edge in graph:
        c, x, y = edge
        if find(parent, x) != find(parent, y):
            union(parent, x, y)
            answer += c
    
    print(answer)