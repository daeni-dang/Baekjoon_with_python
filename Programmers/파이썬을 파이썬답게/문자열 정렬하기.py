'''
ljust(n) : 좌측 정렬
center(n) : 가운데 정렬
rjust(n) : 우측 정렬
'''

s, n = input().strip().split(' ')
n = int(n)
print(s.ljust(n))
print(s.center(n))
print(s.rjust(n))