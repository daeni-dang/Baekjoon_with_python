import heapq
import sys

input = sys.stdin.readline


T = int(input())
for _ in range(T):
    maxheap = []
    minheap = []
    
    k = int(input())
    status = [False] * k
    for i in range(k):
        op, n = map(str, input().split())
        n = int(n)
        if op == "I":
            heapq.heappush(maxheap, (-n, i))
            heapq.heappush(minheap, (n, i))
            status[i] = True
        else:
            if n == 1:
                while maxheap and not status[maxheap[0][1]]:
                    heapq.heappop(maxheap)
                if maxheap:
                    num, idx = heapq.heappop(maxheap)
                    status[idx] = False
            else:
                while minheap and not status[minheap[0][1]]:
                    heapq.heappop(minheap)
                if minheap:
                    num, idx = heapq.heappop(minheap)
                    status[idx] = False
                    

    while maxheap and not status[maxheap[0][1]]:
        heapq.heappop(maxheap)
    while minheap and not status[minheap[0][1]]:
        heapq.heappop(minheap)
        
    if not minheap or not maxheap:
        print("EMPTY")
    else:
        print(-heapq.heappop(maxheap)[0], heapq.heappop(minheap)[0])