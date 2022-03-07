import re

def solution(new_id):
    # Step 1
    new_id = new_id.lower()

    # Step 2
    new_id = re.sub('[^a-z0-9\-_.]', '', new_id)

    # Step 3
    temp = list(new_id)
    for index, letter in enumerate(new_id):
        if letter == '.':
            if index < len(temp) - 1 and new_id[index + 1] == '.':
                temp[index + 1] = ''
    new_id = ''.join(list(filter(lambda letter: letter != '', temp)))

    # Step 4
    new_id = new_id[1:] if new_id[0] == '.' else new_id

    # Step 5
    new_id = 'a' if not new_id else new_id

    # Step 6-1
    if len(new_id) > 15:
        new_id = new_id[:15]

    # Step 6-2
    new_id = new_id[:len(new_id) - 1] if new_id[len(new_id) - 1] == '.' else new_id

    # Step 7
    while len(new_id) < 3:
        new_id += new_id[-1]

    return new_id
