import sys

n = int(input())
student = []
for i in range(n):
    tmp = list(map(str, sys.stdin.readline().rstrip().split()))
    for j in range(1, len(tmp)):
        tmp[j] = int(tmp[j])
    student.append(tmp)
student.sort(key=lambda x : (-x[1], x[2], -x[3], x[0]))
for i in range(n):
    sys.stdout.write(student[i][0] + '\n')