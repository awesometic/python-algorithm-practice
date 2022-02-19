def solution(n, lost, reserve):
    # Create an array for the students
    # Use index as a student number, so that the index 0 will be ignored
    # Firstly, all students have their clothes
    students = [1] * (n + 1)
    students[0] = 0

    # Calculate losts
    for stu in lost:
        students[stu] -= 1

    # Calculate angeles
    for stu in reserve:
        students[stu] += 1

    for stu, count in enumerate(students):
        # Ignore the first index, which is not a student
        if stu == 0:
            continue

        # If current student has nothing,
        if count == 0:
            # Check if the prev person and the next person
            # But ignore if the current student has the last number
            if students[stu - 1] > 1:
                students[stu] += 1
                students[stu - 1] -= 1
            elif stu != n and students[stu + 1] > 1:
                students[stu] += 1
                students[stu + 1] -= 1
            else:
                pass

    # Return the count of who has whose clothes
    return len(list(filter(lambda x: x > 0, students)))
