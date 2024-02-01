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
    return parent

def solution(N, M, nodes):
    parents = [i for i in range(N + 1)]
    for node in nodes:
        parents = union(parents, node[0], node[1])
    for i in range(1, N + 1):
        parents[i] = find(parents, i)
    return len(set(parents[1:]))
    

def main():
    N, M = map(int, input().split())
    nodes = []
    for _ in range(M):
        nodes.append(list(map(int, input().split())))
    print(solution(N, M, nodes))

if __name__ == "__main__":
    main()