def solution(board, moves):
    basket = []
    answer = 0

    for pick in moves:
        rowIdxOfPick = pick - 1
        for row in board:
            if row[rowIdxOfPick] != 0:
                if basket and basket[-1] == row[rowIdxOfPick]:
                    answer += 2
                    basket.pop()
                else:
                    basket.append(row[rowIdxOfPick])

                row[rowIdxOfPick] = 0
                break

    return answer