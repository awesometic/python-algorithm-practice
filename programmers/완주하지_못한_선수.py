def solution(participant, completion):
    part_dict = {}

    for person in participant:
        if person in part_dict:
            part_dict[person] += 1
        else:
            part_dict[person] = 1

    for person in completion:
        if person in part_dict:
            part_dict[person] -= 1
            if part_dict[person] == 0:
                del part_dict[person]

    answer = ""
    for person, count in part_dict.items():
        if count == 1:
            answer = person

    return answer
