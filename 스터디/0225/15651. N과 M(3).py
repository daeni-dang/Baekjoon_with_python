import sys
input = sys.stdin.readline

def permutation(depth, j):
    if depth == M:
        print(' '.join(map(str, arr)))
        return
    for i in range(1, N + 1):
        arr.append(i)
        permutation(depth + 1, i + 1)
        arr.pop()

def solution(N, M):
    permutation(0, 1)

def main():
    global N, M
    N, M = map(int, input().split())
    solution(N, M)

if __name__ == "__main__":
    N, M = 0, 0
    arr = []
    main()