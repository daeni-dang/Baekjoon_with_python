n = int(input())
num = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

min_value = 1000000000
max_value = -1000000000

def dfs(i, cur):
    global add, sub, mul, div, min_value, max_value
    if i == n:
        min_value = min(min_value, cur)
        max_value = max(max_value, cur)
        return
    if add > 0:
        add -= 1
        dfs(i + 1, cur + num[i])
        add += 1
    if sub > 0:
        sub -= 1
        dfs(i + 1, cur - num[i])
        sub += 1
    if mul > 0:
        mul -= 1
        dfs(i + 1, cur * num[i])
        mul += 1
    if div > 0:
        div -= 1
        dfs(i + 1, cur // num[i])
        div += 1
dfs(1, num[0])
print(max_value)
print(min_value)