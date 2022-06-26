t = int(input()) # 테스트 케이스 개수
for _ in range(t):
    k = int(input()) # 층 (0~)
    n = int(input()) # 호 (1~)
    zero = [z for z in range(1, n + 1)] # 0층
    for i in range(k):          # 층
        for j in range(1, n):   # 호
            zero[j] += zero[j - 1]
    print(zero[n - 1])