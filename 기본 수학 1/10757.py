# a, b = input().split()
#
# big = max(len(a), len(b))
# result = ""
# up = 0
#
# for i in range(big):
#     if i >= len(a):
#         result += str(up + int(b[len(b) - 1 - i]))
#         up = 0
#     elif i >= len(b):
#         result += str(up + int(a[len(a) - 1 - i]))
#         up = 0
#     else:
#         each = int(a[len(a) - 1 - i]) + int(b[len(b) - 1 - i])
#         result += str((up + each) % 10)
#         if each > 9 or (each == 9 and up == 1):
#             up = 1
#         else: up = 0
#
# if up == 1:
#     result += str(up)
#
# print(''.join(reversed(result)))

a, b = map(int, input().split())
print(a+b)