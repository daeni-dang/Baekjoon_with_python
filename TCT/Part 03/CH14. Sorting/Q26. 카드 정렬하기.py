import heapq
import sys

n = int(input())
card = []
for i in range(n):
    heapq.heappush(card, int(sys.stdin.readline()))
answer = 0
while len(card) > 1:
    first = heapq.heappop(card)
    second = heapq.heappop(card)
    heapq.heappush(card, (first + second))
    answer += first + second
print(answer)