def solution(record):
    answer = []
    userDict = {}

    for element in record:
        splited = element.split(' ')

        if splited[0] == 'Enter' or splited[0] == 'Change':
            userDict[splited[1]] = splited[2]

    for element in record:
        splited = element.split(' ')

        if splited[0] == 'Enter':
            answer.append(userDict[splited[1]] + '님이 들어왔습니다.')
        elif splited[0] == 'Leave':
            answer.append(userDict[splited[1]] + '님이 나갔습니다.')

    return answer
