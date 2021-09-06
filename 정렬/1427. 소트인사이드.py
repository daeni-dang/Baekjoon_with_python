import sys
str = sys.stdin.readline()
num = list(str)
num.sort(reverse=True)
sys.stdout.write(''.join(num) + '\n')