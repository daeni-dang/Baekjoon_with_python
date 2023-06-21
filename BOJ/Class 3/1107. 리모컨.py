N = int(input())
M = int(input())
if M == 0:
    answer = len(str(N))
else:
    answer = abs(N - 100)
    button = list(map(int, input().split()))

    b = [True] * 10
    for i in button:
        b[i] = False

    for i in range(1000001):
        for j in str(i):
            if not b[int(j)]:
                break
        else:
            answer = min(answer, len(str(i)) + abs(i - N))

print(answer)