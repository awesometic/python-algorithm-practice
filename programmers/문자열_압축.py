def solution(s):
    answer = []

    # Upside-down floor division to get the ceil instead
    maxCompNum = -(len(s) // -2)

    for compNum in range(1, maxCompNum + 1):
        compressed = ''
        i = 0

        while i < len(s):
            compTarget = s[i:i + compNum]

            repeated = 1
            for j in range(1, len(s)):
                if compTarget == s[i + (j * compNum):i + (j * compNum) + compNum]:
                    repeated += 1
                else:
                    break

            if repeated > 1:
                compressed += str(repeated) + compTarget
                i += (repeated * compNum)
            else:
                compressed += s[i:i + compNum]
                i += compNum

        answer.append(len(compressed))

    return min(answer)
