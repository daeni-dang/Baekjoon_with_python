result = 1

def factorial(n):
    global result
    result *= n
    if n == 1:
        return
    return factorial(n - 1)

a = int(input())
if a == 0:
    result = 1
else:
    factorial(a)
print(result)