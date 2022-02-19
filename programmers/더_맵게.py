import heapq


def solution(scoville, K):
    answer = 0

    # Convert the givien scoville list to heap
    heapq.heapify(scoville)

    while True:
        # If there is only one food left and that is not spicy as scoville K
        if len(scoville) == 1 and scoville[0] < K:
            answer = -1
            break

        allNotSpicy = True
        for i, food in enumerate(scoville):
            if food < K:
                mostNotSpicy = heapq.heappop(scoville)
                secondNotSpicy = heapq.heappop(scoville)

                heapq.heappush(scoville, mostNotSpicy + (secondNotSpicy * 2))
                answer += 1
                break

            # If each scoville level is satisfied with K
            if i == len(scoville) - 1:
                allNotSpicy = False

        # If all the food is spicy as scoville K
        if not allNotSpicy:
            break

    return answer
