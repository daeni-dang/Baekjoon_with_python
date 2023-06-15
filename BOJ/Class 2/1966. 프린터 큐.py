from collections import deque
import sys
input = sys.stdin.readline

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        tmp = list(map(int, input().split()))
        doc = deque()
        for idx, imp in enumerate(tmp):
            doc.append([idx, imp])
        tmp.sort(reverse=True)
        impIdx = 0
        cnt = 0
        while True:
            idx, imp = doc.popleft()
            if imp < tmp[impIdx]:
                doc.append([idx, imp])
            elif imp >= tmp[impIdx]:
                impIdx += 1
                cnt += 1
                if idx == M:
                    print(cnt)
                    break
            