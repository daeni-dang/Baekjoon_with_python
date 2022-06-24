def findMax(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    elif c > a and c > b:
        return c

a, b, c = map(int, input().split())
if a == b and b == c:
    print(10000 + a * 1000)
elif a == b:
    print(1000 + a * 100)
elif b == c:
    print(1000 + b * 100)
elif a == c:
    print(1000 + c * 100)
else:
    big = findMax(a, b, c)
    print(big * 100)