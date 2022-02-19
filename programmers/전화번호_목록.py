def solution(phone_book):
    # If all the phone numbers have the same length
    # This reduces the running time of efficiency test #3, from about 120ms to about 15ms
    if len(set(list(map(lambda x: len(x), phone_book)))) == 1:
        return True

    # Sort, then the phone numbers are ordered by string priority
    # The lower number is moved to the front of the array
    # This means, "0123" will be at the front rather than "0123456" or "1234"
    phone_book.sort()

    for index, phone in enumerate(phone_book):
        if index == len(phone_book) - 1:
            break

        # So that the next number will be the exact/almost same number with the current number
        if phone == phone_book[index + 1][: len(phone)]:
            return False

    return True
