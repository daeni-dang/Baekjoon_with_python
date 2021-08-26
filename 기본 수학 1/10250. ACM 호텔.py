t = int(input())

for i in range(t):
    h, w, n = input().split()
    h = int(h)
    w = int(w)
    n = int(n)

    room = n // h + 1
    floor = n % h
    if floor == 0:
        floor += h
        room -= 1
    if room < 10:
        room = '0' + str(room)
    print(str(floor) + str(room))