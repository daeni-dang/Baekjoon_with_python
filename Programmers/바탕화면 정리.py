def solution(wallpaper):
    answer = []
    left, right, top, bottom = 51, 0, 51, 0 
    for x, i in enumerate(wallpaper):
        for y, j in enumerate(i):
            if j == "#":
                if x < top:
                    top = x
                if x > bottom:
                    bottom = x
                if y > right:
                    right = y
                if y < left:
                    left = y
    answer = [top, left, bottom + 1, right + 1]
    return answer