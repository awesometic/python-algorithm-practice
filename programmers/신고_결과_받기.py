def solution(id_list, report, k):

    # Remove duplicates so that this makes sure that a user
    # can report another user only once
    report = list(set(report))

    villain = {}
    for name in id_list:
        villain[name] = 0

    for item in report:
        name = item.split()[1]
        villain[name] += 1

    answer = [0] * len(id_list)
    for item in report:
        reporterName, villainName = item.split()
        # If the reported name is suspended,
        # add 1 to the corresponded index of the answer list
        if villain[villainName] >= k:
            answer[id_list.index(reporterName)] += 1

    return answer
