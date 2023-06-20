import sys
from collections import deque
input = sys.stdin.readline

def topological():
    answer = []
    q = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        tmp = q.popleft()
        answer.append(tmp)
        for i in graph[tmp]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    return answer

def makeGraph():
    for i in range(n + 1):
        present[i] = False
    for _ in range(m):
        s, *arr = map(int, input().split())
        for i in range(s - 1):
            graph[arr[i]].append(arr[i + 1])
            indegree[arr[i + 1]] += 1

if __name__ == "__main__":
    n, m = map(int, input().split())

    present = {}
    graph = [[] for _ in range(n + 1)]
    indegree = [0] * (n + 1)
    
    makeGraph()
    answer = topological()
    if len(answer) < n:
        print(0)
    else:
        for i in answer:
            print(i)

    