from collections import deque

if __name__ == "__main__":
    N, K = map(int, input().split())
    M = len(str(N))
    q = deque([[N, 0]])
    visited = set()
    answer = 0
    
    while q:
        cur, k = q.popleft()
        if k == K:
            answer = max(answer, cur)
            continue
        arr = list(str(cur))
        for i in range(M - 1):
            for j in range(i + 1, M):
                if i == 0 and arr[j] == "0":
                    continue
                
                arr[i], arr[j] = arr[j], arr[i]
                intArr = int(''.join(arr))
                if (intArr, k + 1) not in visited:
                    q.append([intArr, k + 1])
                    visited.add((intArr, k + 1))
                arr[i], arr[j] = arr[j], arr[i]
        
        
    print(answer if answer > 0 else -1)