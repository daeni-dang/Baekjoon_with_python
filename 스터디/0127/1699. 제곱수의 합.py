'''
    참고 : https://lakelouise.tistory.com/61#google_vignette
'''

import sys
input = sys.stdin.readline

def solution(n):
    dp = [i for i in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, i):
            if j * j > i:
                break
            if dp[i] > dp[i - j * j] + 1:
                dp[i] = dp[i - j * j] + 1
    return dp[n]

def main():
    n = int(input())
    print(solution(n))

if __name__ == "__main__":
    main()