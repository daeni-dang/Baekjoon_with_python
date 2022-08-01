point = input()

first, second = point[0], point[1]

move = [[2, 1], [2, -1],
        [-2, 1], [-2, -1],
        [1, 2], [1, -2],
        [-1, 2], [-1, -2]]
count = 0

for m in move:
    tmp1 = chr(ord(first) + m[0])
    tmp2 = chr(ord(second) + m[1])
    if 'a' <= tmp1 <= 'h' and '1' <= tmp2 <= '8':
        count += 1
print(count)
