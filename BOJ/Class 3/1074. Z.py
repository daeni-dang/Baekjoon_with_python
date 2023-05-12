def function(N, r, c):
    tmp = 0
    while N > 1:
        size = (2 ** N) // 2
        # 2사분면
        if r < size and c < size:
            pass
        # 1사분면
        elif r < size and c >= size:
            tmp += size ** 2
            c -= size
        # 3사분면
        elif r >= size and c < size:
            tmp += (size ** 2) * 2
            r -= size
        # 4사분면
        else:
            tmp += (size ** 2) * 3
            r -= size
            c -= size
        N -= 1
    
    if r == 0 and c == 0:
        return tmp
    elif r == 0 and c == 1:
        return tmp + 1
    elif r == 1 and c == 0:
        return tmp + 2
    else:
        return tmp + 3
        

if __name__ == "__main__":
    N, r, c = map(int, input().split())
    
    print(function(N, r, c))