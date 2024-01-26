import sys
input = sys.stdin.readline

def solution(n, arr):
    dp = [arr[i] for i in range(n)]
    for i in range(n):
        for j in range(i, n):
            if arr[i] < arr[j]:
                dp[j] = max(dp[j], dp[i] + arr[j])
    return max(dp)

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    print(solution(n, arr))

if __name__ == "__main__":
    main()