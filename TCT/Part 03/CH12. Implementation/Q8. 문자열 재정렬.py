s = input()

alp = []
num = []
for i in s:
    if 'a' <= i <= 'z' or 'A' <= i <= 'Z':
        alp.append(i)
    else:
        num.append(int(i))
alp.sort()
for i in alp:
    print(i, end="")
print(sum(num))