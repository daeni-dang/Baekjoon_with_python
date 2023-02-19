'''
divmod(x, y) : 몫과 나머지를 tuple 형식으로 반환
unpacking(*) : divmod에서 반환된 튜플을 unpacking
'''

a, b = map(int, input().strip().split(' '))
print(*divmod(a, b))