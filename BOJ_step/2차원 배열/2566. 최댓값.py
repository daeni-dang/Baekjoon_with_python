max_value = -1
max_x, max_y = 0, 0

for i in range(9):
    num = map(int, input().split())
    for idx, j in enumerate(num):
        if j > max_value:
            max_value = j
            max_x = i + 1
            max_y = idx + 1
            
print(max_value)
print(max_x, max_y)