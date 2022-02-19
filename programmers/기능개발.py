import math


def solution(progresses, speeds):
    answer = []
    est = []

    for i in range(0, len(progresses)):
        est.append(math.ceil((100 - progresses[i]) / speeds[i]))

    firstDueDate = -1
    finishedJobs = 0
    for i, due in enumerate(est):
        if i == 0:
            firstDueDate = due

        if firstDueDate >= due:
            finishedJobs += 1
        else:
            answer.append(finishedJobs)
            firstDueDate = due
            finishedJobs = 1

    answer.append(finishedJobs)
    return answer
