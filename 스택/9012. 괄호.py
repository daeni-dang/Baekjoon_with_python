import sys
n = int(sys.stdin.readline())
for i in range(n):
    paran = sys.stdin.readline().strip()

    stack = []
    flag = True
    if paran.count('(') != paran.count(')'):
        flag = False
    else:
        for j in range(len(paran)):
            if paran[j] == '(':
                stack.append(paran[j])
            if paran[j] == ')':
                if len(stack) == 0:
                    flag = False
                else:
                    stack.pop()
    if flag:
        sys.stdout.write("YES" + '\n')
    else:
        sys.stdout.write("NO" + '\n')