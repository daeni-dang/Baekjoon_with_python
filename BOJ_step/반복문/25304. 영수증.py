X = int(input())
N = int(input())
total = 0
for i in range(N):
    price, num = map(int, input().split())
    total += price * num
if total == X:
    print("Yes")
else:
    print("No")