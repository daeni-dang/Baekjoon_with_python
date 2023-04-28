import heapq
import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    maxHeap = []
    minHeap = []
    maxlength, minlength = 0, 0
    for i in range(n):
        num = int(sys.stdin.readline())
        if maxlength == 0:
            heapq.heappush(maxHeap, -num)
            maxlength += 1
        else:
            if maxlength > minlength:
                heapq.heappush(minHeap, num)
                minlength += 1
            else:
                heapq.heappush(maxHeap, -num)
                maxlength += 1
        if maxHeap and minHeap and -maxHeap[0] > minHeap[0]:
            maxTop = heapq.heappop(maxHeap)
            minTop = heapq.heappop(minHeap)
            heapq.heappush(maxHeap, -minTop)
            heapq.heappush(minHeap, -maxTop)
            
        sys.stdout.write(str(-maxHeap[0]) + "\n")