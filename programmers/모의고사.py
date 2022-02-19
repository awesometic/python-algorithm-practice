def solution(answers):
    strategies = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5],
    ]
    hitCounts = [0, 0, 0]

    for i, answer in enumerate(answers):
        hitCounts[0] += 1 if strategies[0][i % len(strategies[0])] == answer else 0
        hitCounts[1] += 1 if strategies[1][i % len(strategies[1])] == answer else 0
        hitCounts[2] += 1 if strategies[2][i % len(strategies[2])] == answer else 0

    answer = []
    maxHitCount = max(hitCounts)
    for i, count in enumerate(hitCounts):
        if maxHitCount == count:
            answer.append(i + 1)

    print(f"{hitCounts},{answer}")

    return answer
