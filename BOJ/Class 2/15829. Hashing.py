L = int(input())
arr = input()

sum = 0
for i in range(L):
    sum += ((ord(arr[i]) - 96) * (31 ** i))
print(sum % 1234567891)