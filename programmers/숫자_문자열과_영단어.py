def solution(s):
    answer = ''

    engAndNumMap = {
        '0': 'zero',
        '1': 'one',
        '2': 'two',
        '3': 'three',
        '4': 'four',
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        '9': 'nine'
    }

    # It is much better to use "replace" function that I forgot
    i = 0
    while i < len(s):
        if s[i] not in engAndNumMap.keys():
            for num, eng in engAndNumMap.items():
               	if eng == s[i:i + len(eng)]:
                    answer += num
                    i += len(eng)
                    break
        else:
            answer += s[i]
            i += 1

    return int(answer)
