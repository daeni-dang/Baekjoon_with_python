import sys
input = sys.stdin.readline

def main():
    i = 1
    while True:
        L, P, V = map(int, input().split())
        if L == 0 and P == 0 and V == 0:
            break
        print(f"Case {i}: {(V // P) * L + min((V % P), L)}")
        i += 1

if __name__ == "__main__":
    main()