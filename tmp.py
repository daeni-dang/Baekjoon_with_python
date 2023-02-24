from collections import deque

n, m = map(int, input().split())
ice = []
for i in range(n):
    ice.append(input())

def bfs(x, y):
    