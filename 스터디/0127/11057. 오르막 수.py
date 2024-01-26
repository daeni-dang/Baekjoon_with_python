import sys
import math
input = sys.stdin.readline

def solution(n):
    return math.comb(10 + n - 1, n) % 10007

def main():
    n = int(input())
    print(solution(n))

if __name__ == "__main__":
    main()