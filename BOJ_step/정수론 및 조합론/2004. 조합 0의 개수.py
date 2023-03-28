n, m = map(int, input().split())

def factorial(num):
    if num == 1:
        return 1
    return num * factorial(num - 1)

result = factorial(n) // (factorial(n - m) * factorial(m))

str_result = str(result)

cnt = 0

for i in range(len(str_result) - 1, 0, -1):
    if str_result[i] == '0':
        cnt += 1
    else:
        break
    
print(cnt)