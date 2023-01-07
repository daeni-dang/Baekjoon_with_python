s1 = input()
s2 = input()

str_map = [[0] * len(s2) for _ in range(len(s1))]

for i in range(len(s1)):
    for j in range(len(s2)):
        if s1[i] == s2[j] and (i == 0 or j == 0):
            str_map[i][j] = 1
        elif s1[i] == s2[j]:
            str_map[i][j] = str_map[i - 1][j - 1] + 1
max_len = 0
for i in range(len(s1)):
    for j in range(len(s2)):
        if str_map[i][j] > max_len:
            max_len = str_map[i][j]

print(max_len)