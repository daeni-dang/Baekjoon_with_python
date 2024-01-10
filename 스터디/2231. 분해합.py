import sys
input = sys.stdin.readline

if __name__ == "__main__":
    answer = 0
    num = int(input())
    
    start, end = 0, num
    while start < end:
        mid = (start + end) // 2
        print(start, end, mid)
        sums = mid
        for i in str(mid):
            sums += int(i)
        if sums == num:
            answer = mid
            break
        elif sums < num:
            start = mid + 1
        else:
            end = mid - 1
    
    # for i in range(num):
    #     sums = i
    #     for j in str(i):
    #         sums += int(j)
    #     if sums == num:
    #         answer = i
    #         break
    print(answer)