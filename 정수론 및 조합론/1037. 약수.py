import sys
n = int(sys.stdin.readline())
num = sys.stdin.readline().split()
for i in range(n):
    num[i] = int(num[i])
sys.stdout.write(str(int(min(num)) * int(max(num))) + '\n')