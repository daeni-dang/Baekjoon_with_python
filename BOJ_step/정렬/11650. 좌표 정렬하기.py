import sys
n = int(sys.stdin.readline())
point = []
for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    point.append([x, y])
point.sort()
for i in point:
    sys.stdout.write(str(i[0]) + ' ' + str(i[1]) + '\n')