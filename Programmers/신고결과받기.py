def solution(id_list, report, k):
    answer = []
    id_report = {}
    for id in id_list:
        id_report[id] = []
    for id in report:
        report_split = id.split(' ')
        if report_split[1] not in id_report[report_split[0]]:
            id_report[report_split[0]].append(report_split[1])
    reported = {}
    for id in id_list:
        reported[id] = 0
    for id in id_list:
        for r_id in id_report[id]:
            reported[r_id] += 1
    stopped = []
    for id in id_list:
        if reported[id] >= k:
            stopped.append(id)
    for id in id_list:
        mail_count = 0
        for s_id in stopped:
            if s_id in id_report[id]:
                mail_count += 1
        answer.append(mail_count)
    return answer