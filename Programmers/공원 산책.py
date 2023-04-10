def solution(park, routes):
    answer = []
    X, Y = len(park), len(park[0])
    S = []
    for i, p in enumerate(park):
        find = p.find("S")
        if find != -1:
            S = [i, find]
    x, y = S
    for route in routes:
        op, n = route.split()
        tmpX, tmpY = x, y
        if op == "N":
            tmpX = x - int(n)
        elif op == "S":
            tmpX = x + int(n)
        elif op == "W":
            tmpY = y - int(n)
        elif op == "E":
            tmpY = y + int(n)
        if tmpX < X and tmpY < Y and tmpX >= 0 and tmpY >= 0:
            if op == "N" or op == "S":
                s, e = min(x, tmpX), max(x, tmpX)
                Xflag = False
                for i in range(s, e+1):
                    if park[i][y] == "X":
                        Xflag = True
                        break
                if not Xflag:
                    x = tmpX
            else:
                s, e = min(y, tmpY), max(y, tmpY)
                if park[x][s:e+1].find("X") == -1:
                    y = tmpY
    answer = [x, y]
    return answer