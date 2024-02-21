import sys
input = sys.stdin.readline

def solution(encoded, strs):
    alps = "abcdefghijklmnopqrstuvwxyz"
    for i in range(1, 27):
        tmp = ""
        for c in encoded:
            tmp += alps[(ord(c) - 97 + i) % 26]
        for s in strs:
            for j in range(len(tmp) - len(s) + 1):
                if tmp[j:j+len(s)] == s:
                    return tmp

def main():
    encoded = input().strip()
    strs = []
    n = int(input())
    for _ in range(n):
        strs.append(input().strip())
    print(solution(encoded, strs))

if __name__ == "__main__":
    main()