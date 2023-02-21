import heapq

def solution(k, score):
    answer = []
    heap = []
    for i in score:
        heapq.heappush(heap, i)
        if len(heap) > k:
            heapq.heappop(heap)
        answer.append(heap[0])
    return answer