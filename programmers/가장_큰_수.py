def merge_sort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2

    # Divide into 2 recursively until there is only one element left
    # And merging it by using...
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    merged_arr = []
    l = h = 0

    while l < len(left) and h < len(right):
        strLeft = str(left[l])
        strRight = str(right[h])

        # Check if which way of string concatenate is larger
        if int(strLeft + strRight) > int(strRight + strLeft):
            # If the number is bigger when the left number is in the left side,
            # Add that number first to the merged_arr
            merged_arr.append(left[l])
            l += 1
        else:
            # In the opposite case
            merged_arr.append(right[h])
            h += 1

    merged_arr += left[l:]
    merged_arr += right[h:]

    return merged_arr


def solution(numbers):
    # Solve this problem using merge sort
    numbers = merge_sort(numbers)

    merged = "".join(map(str, numbers))
    return "0" if merged[0] == "0" else merged
