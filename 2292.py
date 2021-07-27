index = 1
a = int(input())
n = 1
while a > index:
    index += 6 * n
    n = n + 1
    if index > a: break
print(n)