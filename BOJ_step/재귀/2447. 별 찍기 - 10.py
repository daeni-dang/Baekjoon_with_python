def draw_star(n):
    if n == 1:
        return ['*']
    star = draw_star(n // 3)
    arr = []

    for i in star:
        arr.append(i * 3)
    for i in star:
        arr.append(i + ' ' * (n // 3) + i)
    for i in star:
        arr.append(i * 3)
    return arr

if __name__ == '__main__':
    n = int(input())
    print('\n'.join(draw_star(n)))