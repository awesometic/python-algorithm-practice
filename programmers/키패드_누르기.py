from collections import deque


def bfs(keypad, searchFrom, target):
    distance = 0
    queue = deque([searchFrom])

    visited = [False] * 13
    visited[searchFrom] = True

    # If searching reaches to the [2, 5, 8, 0] world,
    # then set this flag True to prevent from accumlating
    # of the distance when it failes to search the target node
    wasInTheWorld = False
    firstFounder = 0

    while queue:
        v = queue.popleft()

        if v in [2, 5, 8, 11] and not wasInTheWorld:
            wasInTheWorld = True
            firstFounder = v

        if v in keypad[firstFounder] and wasInTheWorld:
            if searchFrom == firstFounder:
                distance = 1
            else:
                distance = 2

        if v == target:
            return distance
        else:
            distance += 1
        for i in keypad[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


def solution(numbers, hand):
    answer = ""

    # Assume that '*' is 10, '0' is '11', #' is 12
    keypad = [
        [],
        [2],
        [5],
        [2],
        [5],
        [2, 8],
        [5],
        [8],
        [5, 11],
        [8],
        [11],
        [8],
        [11],
    ]

    # Initial value
    leftHand = 10
    rightHand = 12

    for num in numbers:
        if num in [1, 4, 7]:
            leftHand = num
            answer += "L"
        elif num in [3, 6, 9]:
            rightHand = num
            answer += "R"
        else:
            num = 11 if num == 0 else num

            lenFromLeft = bfs(keypad, leftHand, num)
            lenFromRight = bfs(keypad, rightHand, num)

            print(f"[{num:2}]: {leftHand},{rightHand} | {lenFromLeft},{lenFromRight}")

            if lenFromLeft < lenFromRight:
                leftHand = num
                answer += "L"
            elif lenFromLeft > lenFromRight:
                rightHand = num
                answer += "R"
            else:
                if hand == "left":
                    leftHand = num
                    answer += "L"
                else:
                    rightHand = num
                    answer += "R"

    return answer
