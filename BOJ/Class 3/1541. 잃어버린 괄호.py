arr = input().split("-")

nums = []
for i in arr:
    nums.append(sum(list(map(int, i.split("+")))))

answer = nums[0]
for i in nums[1:]:
    answer -= i
print(answer)