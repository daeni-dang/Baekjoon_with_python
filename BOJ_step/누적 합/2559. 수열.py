import sys
n, k = map(int, sys.stdin.readline().split())
temp = list(map(int, sys.stdin.readline().split()))

sum_list = [sum(temp[:k])]

for i in range(len(temp) - k):
    sum_list.append(sum_list[len(sum_list) - 1] - temp[i] + temp[i + k])
sys.stdout.write(str(max(sum_list)))