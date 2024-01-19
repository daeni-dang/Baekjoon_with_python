'''
    참고 : https://journeytosth.tistory.com/16
'''

import sys
input = sys.stdin.readline

def main():
    answer = 0
    N = int(input())
    K = int(input())
    sensors = list(map(int, input().split()))
    if K >= N:
        answer = 0
    else:
        sensors.sort()
        intervals = [sensors[i + 1] - sensors[i] for i in range(N - 1)]
        intervals.sort()
        for _ in range(K - 1):
            intervals.pop()
        answer = sum(intervals)
    print(answer)

if __name__ == "__main__":
    main()