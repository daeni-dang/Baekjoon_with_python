import sys
n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().strip().split()))
num2 = sorted(set(num))
dic = {num2[i] : i for i in range(len(num2))}
for i in num:
    sys.stdout.write(str(dic[i]) + ' ')