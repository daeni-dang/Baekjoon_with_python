'''
int(string, base) : string을 base진법으로 변환
'''

num, base = map(int, input().strip().split(' '))
print(int(str(num), base))