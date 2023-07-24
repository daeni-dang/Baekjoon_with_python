import sys
import heapq
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
q = []
for _ in range(N):
    num = int(input())
    if num == 0:
        if len(q) == 0:
            print(str(0) + "\n")
        else:
            print(str(heapq.heappop(q)[1]) + "\n")
    else:
        heapq.heappush(q, (abs(num), num))
    