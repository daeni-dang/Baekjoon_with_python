n = int(input())
arr = list(map(int, input().split()))
arr.sort()

member = 1
group = 0
for i in arr:
    if i > member:
        member += 1
    else:
        member = 1
        group += 1
print(group)