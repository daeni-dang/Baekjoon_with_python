n = int(input())
move = list(input().split())
cur = [1, 1]
dict = {'L' : [0, -1], 'R' : [0, 1], 'U' : [-1, 0], 'D' : [1, 0]}

for m in move:
    first = cur[0] + dict[m][0]
    second = cur[1] + dict[m][1]
    if 0 < first <= n and 0 < second <= n:
        cur[0] += dict[m][0]
        cur[1] += dict[m][1]

print(cur)