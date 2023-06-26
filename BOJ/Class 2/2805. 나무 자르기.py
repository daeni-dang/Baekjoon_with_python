if __name__ == "__main__":
    N, M = map(int, input().split())
    trees = list(map(int, input().split()))
    
    start, end = 1, max(trees)
    answer = 0
    while start <= end:
        mid = (start + end) // 2
        tmp = 0
        for tree in trees:
            if tree > mid:
                tmp += tree - mid
        if tmp == M:
            answer = mid
            break
        elif tmp > M:
            start = mid + 1
            answer = max(answer, mid)
        else:
            end = mid - 1
    print(answer)