def sort(num):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(num) - 1):
            if num[i] > num[i + 1]:
                tmp = num[i]
                num[i] = num[i + 1]
                num[i + 1] = tmp
                sorted = False
    return num

n = int(input())
num = []
for i in range(n):
    a = int(input())
    num.append(a)
num = sort(num)
for i in range(len(num)):
    print(num[i])