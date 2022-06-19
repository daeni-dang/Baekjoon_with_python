hour, min = map(int, input().split())
need = int(input())

min += need
while min > 59:
    hour += 1
    min -= 60
if hour > 23:
    hour -= 24

print(hour, min)