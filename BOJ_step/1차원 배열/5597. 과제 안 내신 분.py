stu = [0] * 30
for i in range(28):
    stu[int(input()) - 1] = 1
no = []
for i in range(30):
    if stu[i] == 0:
        no.append(i + 1)
no.sort()
for i in no:
    print(i)