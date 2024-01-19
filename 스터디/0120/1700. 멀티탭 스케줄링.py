from collections import defaultdict, deque
import sys
input = sys.stdin.readline

def main():
    answer = 0
    N, K = map(int, input().split())
    used = list(map(int, input().split()))
    usingIdx = defaultdict(deque)
    for i in range(K):
        usingIdx[used[i]].append(i)
    multi = [0] * N
    multiRest = N
    for i in range(K):
        # 비어있다면,
        if multiRest > 0:
            if used[i] in multi:
                usingIdx[used[i]].popleft()
                continue
            for j in range(N):
                # 꽂혀있지 않는 전기용품이라면,
                if multi[j] == 0:
                    # 꽂고, 남은 자리 -1
                    multi[j] = used[i]
                    usingIdx[used[i]].popleft() # 현재 인덱스의 값 제거
                    multiRest -= 1
                    break
        # 비어있지 않다면, 가장 미래에 사용하는 것을 뺴기
        else:
            if used[i] in multi:
                usingIdx[used[i]].popleft()
                continue
            maxValue, maxIdx = 0, 0
            for j in range(N):
                if len(usingIdx[multi[j]]) > 0:
                    if usingIdx[multi[j]][0] > maxValue:
                        maxValue = usingIdx[multi[j]][0]
                        maxIdx = j
                else:
                    maxValue = 1e9
                    maxIdx = j
                    break
            multi[maxIdx] = used[i]    # 가장 미래에 사용하는 멀티탭 구에 현재 제품 꽂아주고
            usingIdx[used[i]].popleft()    # 현재 인덱스의 값 제거
            answer += 1
    print(answer)

if __name__ == "__main__":
    main()