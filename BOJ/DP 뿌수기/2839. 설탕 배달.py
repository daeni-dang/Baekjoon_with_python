n = int(input())

dp = [5001] * (n + 5)   # 5보다 작은 입력일 경우 예외처리
dp[3], dp[5] = 1, 1 # 3과 5는 한 번이 최소

for i in range(6, n + 1):
    dp[i] = min(dp[i - 3], dp[i - 5]) + 1

print(dp[n] if dp[n] < 5001 else -1)