import sys
input = sys.stdin.readline

while True:
    num = input().strip()
    if num == "0":
        break
    n = len(num)
    flag = False
    for i in range(n // 2):
        if num[i] != num[n - i - 1]:
            print("no")
            flag = True
            break
    if not flag:
        print("yes")