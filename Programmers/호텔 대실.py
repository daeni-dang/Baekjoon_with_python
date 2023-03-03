def solution(book_time):
    answer = 0
    book_time.sort()
    checkout = []
    for book in book_time:
        in_hour, in_min = book[0].split(":")
        out_hour, out_min = book[1].split(":")
        checkin_time = int(in_hour) * 60 + int(in_min)
        checkout_time = int(out_hour) * 60 + int(out_min) + 10
        if len(checkout) == 0:
            checkout.append(checkout_time)
            continue
        flag = True
        for out in range(len(checkout)):
            if checkin_time >= checkout[out]:
                flag = False
                checkout[out] = checkout_time
                break
        if flag:
            checkout.append(checkout_time)
    answer = len(checkout)
    return answer