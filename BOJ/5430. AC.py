from collections import deque
import sys

def solution(p, n, arr):
    length = n
    reversed = 0
    for i in p:
        if i == "D":
            try:
                if reversed % 2 == 1:
                    arr.pop()
                else:
                    arr.popleft()
                length -= 1
            except:
                return "error"
        else:
            reversed += 1
    if reversed % 2 == 1:
        arr.reverse()
    return "["+",".join(arr)+"]"


if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        p = sys.stdin.readline().strip()
        n = int(sys.stdin.readline())
        arr = sys.stdin.readline().strip()[1:-1]
        if arr != "":
            arr = deque(arr.split(","))
            sys.stdout.write(str(solution(p, n, arr)) + "\n")
        else:
            tmp = p.find("D")
            if tmp != -1:
                sys.stdout.write("error"+"\n")
            else:
                sys.stdout.write("[]"+'\n')