import sys

n = int(input())

def is_good(s):
    for i in range(1, len(s) + 1):
        if s[-i:] == s[-2*i:-i]:
            return False
    return True


def good(s):
    if len(s) == n:
        print(s)
        exit()
    for i in "123":
        if is_good(s + i):
            good(s + i)

good("1")
good("2")
good("3")