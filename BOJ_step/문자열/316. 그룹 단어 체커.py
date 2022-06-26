n = int(input())
cnt = 0

for i in range(n):
    str = input()
    before = ""
    flag = True
    for j in range(len(str)):
        if before.find(str[j]) != -1 and str[j] != str[j - 1]:
            flag = False

        before += str[j]
    if flag:
        cnt = cnt + 1
print(cnt)
