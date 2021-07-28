a, b, v = input().split()
a = int(a)
b = int(b)
v = int(v)

print(int((v - b - 1) / (a - b) + 1))