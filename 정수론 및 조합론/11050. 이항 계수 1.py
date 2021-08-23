def factorial(n, result):
    result *= n
    if n == 1:
        return result
    return factorial(n - 1, result)

n, k = map(int, input().split())
if n == k:
    print(1)
elif k == 0:
    print(1)
else:
    up = factorial(n, 1)
    down = factorial(k, 1)*factorial(n - k, 1)
    print(int(up) // int(down))