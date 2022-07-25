from collections import deque

n = int(input())
queue = deque()

for i in range(n):
    queue.append(i + 1)
for i in range(n - 1):
    queue.popleft()
    tmp = queue.popleft()
    queue.append(tmp)
print(queue[0])