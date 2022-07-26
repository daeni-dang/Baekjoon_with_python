import sys
from collections import deque
n = int(input())
queue = deque()
for i in range(n):
    command = sys.stdin.readline().strip().split()
    if "push" in command:
        queue.append(command[1])
    elif command[0] == "pop":
        if len(queue) == 0:
            sys.stdout.write(str(-1) + '\n')
        else:
            sys.stdout.write(queue.popleft() + '\n')
    elif command[0] == "size":
        sys.stdout.write(str(len(queue)) + '\n')
    elif command[0] == "empty":
        if len(queue) == 0:
            sys.stdout.write(str(1) + '\n')
        else:
            sys.stdout.write(str(0) + '\n')
    elif command[0] == "front":
        if len(queue) == 0:
            sys.stdout.write(str(-1) + '\n')
        else:
            sys.stdout.write(queue[0] + '\n')
    elif command[0] == "back":
        if len(queue) == 0:
            sys.stdout.write(str(-1) + '\n')
        else:
            sys.stdout.write(queue[len(queue) - 1] + '\n')