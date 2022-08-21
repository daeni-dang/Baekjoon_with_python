n = int(input())

score = str(n)

first = score[:len(score) // 2]
last = score[len(score) // 2:]

first_sum, last_sum = 0, 0
for i in range(len(score) // 2):
    first_sum += int(first[i])
    last_sum += int(last[i])
if first_sum == last_sum:
    print("LUCKY")
else:
    print("READY")