import sys


def f():
    flag = True
    while True:
        sen = sys.stdin.readline()
        bracket = []
        if sen == '.\n':
            break
        for i in range(0, len(sen) - 1):
            if sen[i] == '(':
                bracket.append('(')
            elif sen[i] == ')':
                if len(bracket) != 0 and bracket[len(bracket) - 1] == '(':
                    bracket.pop()
                else:
                    flag = False
                    break
            elif sen[i] == '[':
                bracket.append('[')
            elif sen[i] == ']':
                if len(bracket) != 0 and bracket[len(bracket) - 1] == '[':
                    bracket.pop()
                else:
                    flag = False
                    break
        if len(bracket) == 0 and flag is True:
            sys.stdout.write("yes" + '\n')
        else: sys.stdout.write("no" + '\n')

        flag = True

f()