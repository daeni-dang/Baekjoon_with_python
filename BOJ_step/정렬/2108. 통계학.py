import sys
from collections import Counter

n = int(sys.stdin.readline())
num = []
for i in range(n):
    num.append(int(sys.stdin.readline()))
num.sort()

sys.stdout.write(str(round(sum(num) / n)) + '\n')
sys.stdout.write(str(num[n // 2]) + '\n')
mode = Counter(num).most_common()
if len(mode) > 1 and mode[0][1] == mode[1][1]:
    sys.stdout.write(str(mode[1][0]) + '\n')
else:
    sys.stdout.write(str(mode[0][0]) + '\n')
sys.stdout.write(str(max(num) - min(num)) + '\n')
