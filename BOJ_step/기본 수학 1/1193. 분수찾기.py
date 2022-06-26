n = int(input())

num = 1
tmp = 0
diagonal_num = 1
where = 0

while num <= n:
    tmp = num
    num += diagonal_num
    diagonal_num += 1

diagonal_num -= 1
where = n - tmp + 1

sum = diagonal_num + 1
if diagonal_num % 2 == 1:
    sum = sum // 2
    if sum == where:
        print(str(sum)+'/'+str(sum))
    elif sum < where:
        print(str(sum-(where-sum))+'/'+str(sum+(where-sum)))
    else:
        print(str(sum + (sum - where)) + '/' + str(sum - (sum - where)))
else:
    sum = sum // 2
    if sum == where:
        print(str(sum) + '/' + str(sum + 1))
    elif sum < where:
        print(str(sum + (where - sum)) + '/' + str(sum - (where - sum) + 1))
    else:
        print(str(sum - (sum - where)) + '/' + str(sum + (sum - where) + 1))