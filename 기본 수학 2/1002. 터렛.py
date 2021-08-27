t = int(input())
for i in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    if (x1, y1, r1) == (x2, y2, r2):
        print(-1)
    elif dist > r1 + r2 or dist <= abs(r1 - r2) or ((x1, y1) == (x2, y2) and r1 != r2):
        if dist == abs(r1 - r2):
            print(1)
        else: print(0)
    elif dist == r1 + r2:
        print(1)
    elif dist < r1 + r2:
        print(2)
    else: print(2)