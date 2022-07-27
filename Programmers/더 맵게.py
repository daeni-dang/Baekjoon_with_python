import heapq

def solution(scoville, K):
    answer = 0
    heap = []
    for i in scoville:
        heapq.heappush(heap, i)
    try:
        while True:
            least = heapq.heappop(heap)
            if least < K:
                second = heapq.heappop(heap)
                heapq.heappush(heap, least + second * 2)
                answer += 1
            else: break
    except IndexError:
        answer = -1
    return answer