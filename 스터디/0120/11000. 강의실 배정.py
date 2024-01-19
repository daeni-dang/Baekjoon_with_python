import heapq
import sys
input = sys.stdin.readline

def main():
    N = int(input())
    lectures = []
    for _ in range(N):
        lectures.append(list(map(int, input().split())))
    heapq.heapify(lectures)
    ends = [heapq.heappop(lectures)[1]]
    while lectures:
        s, e = heapq.heappop(lectures)
        if s >= ends[0]:    # heap의 가장 작은 수
            heapq.heappushpop(ends, e)
        else:
            heapq.heappush(ends, e)
    print(len(ends))

if __name__ == "__main__":
    main()