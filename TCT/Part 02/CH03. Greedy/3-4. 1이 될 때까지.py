n, k = map(int, input().split())
answer = 0

while n >= k:
    tmp = (n // k) * k
    answer += n - tmp
    n = tmp
    n //= k
    answer += 1
    
print(answer)