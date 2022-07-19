import sys
n, m = map(int, sys.stdin.readline().split())
number = list(map(int, sys.stdin.readline().split()))
sum_list = [0]
sum = 0
for i in range(n):
    sum += number[i]
    sum_list.append(sum)
for i in range(m):
    sidx, lidx = map(int, sys.stdin.readline().split())
    print(sum_list[lidx] - sum_list[sidx - 1])