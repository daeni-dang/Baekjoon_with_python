import sys
input = sys.stdin.readline

def binary():
    start, end = 1, max(lan)
    while start <= end:
        mid = (start + end) // 2
        tmp = 0
        for i in lan:
            tmp += i // mid
        if tmp < N:
            end = mid - 1
        elif tmp >= N:
            start = mid + 1
    return end

if __name__ == "__main__":
    K, N = map(int, input().split())
    lan = []
    for i in range(K):
        lan.append(int(input()))
    print(binary())