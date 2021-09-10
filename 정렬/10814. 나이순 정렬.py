import sys
n = int(sys.stdin.readline())
online = []
for i in range(n):
    age, name = map(str, sys.stdin.readline().split())
    age = int(age)
    online.append([age, name])
online.sort(key=lambda x: x[0])
for i in online:
    sys.stdout.write(str(i[0]) + ' ' + i[1] + '\n')