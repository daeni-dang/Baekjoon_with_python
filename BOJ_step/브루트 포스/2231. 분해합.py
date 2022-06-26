def each_sum(n):
    sum = 0
    for i in range(len(n)):
        sum += int(n[i])
    return sum
n = int(input())
sum = {}
for i in range(n):
    sum[i + 1] = i + 1 + int(each_sum(str(i + 1)))
candidate = []

for key, value in sum.items():
    if value == n:
        candidate.append(key)
if len(candidate) == 0:
    print(0)
else: print(min(candidate))