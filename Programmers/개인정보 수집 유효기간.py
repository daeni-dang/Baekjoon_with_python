def solution(today, terms, privacies):
    answer = []
    terms_dict = {}
    for i in terms:
        tmp = i.split()
        terms_dict[tmp[0]] = tmp[1]
    today_year, today_month, today_day = map(int, today.split('.'))
    
    for idx, i in enumerate(privacies):
        tmp = i.split()
        year, month, day = map(int, tmp[0].split('.'))
        month_tmp = month + int(terms_dict[tmp[1]])
        month = month_tmp % 12
        year = year + month_tmp // 12
        print(year, month, day)
        if month == 0:
            month = 12
            year -= 1
        if year < today_year:
            answer.append(idx + 1)
        elif year == today_year and month < today_month:
            answer.append(idx + 1)
        elif year == today_year and month == today_month and day <= today_day:
            answer.append(idx + 1)
        
    return answer