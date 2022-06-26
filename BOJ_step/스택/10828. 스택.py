import sys
n = int(sys.stdin.readline())
st = []
for i in range(n):
    op = sys.stdin.readline().strip()
    if "push" in op:
        st.append(op.split()[1])
    elif op == "pop":
        if len(st) == 0:
            sys.stdout.write(str(-1) + "\n")
        else: sys.stdout.write(st.pop() + "\n")
    elif op == "size":
        sys.stdout.write(str(len(st)) + "\n")
    elif op == "empty":
        if len(st) == 0:
            sys.stdout.write(str(1) + "\n")
        else: sys.stdout.write(str(0) + "\n")
    elif op == "top":
        if len(st) == 0:
            sys.stdout.write(str(-1)+"\n")
        else: sys.stdout.write(str(st[len(st) - 1])+"\n")