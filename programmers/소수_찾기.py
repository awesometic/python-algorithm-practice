from itertools import permutations


def isPrime(num):
    for i in range(2, num):
        if num % i == 0:
            return False

    return True


def solution(numbers):
    answer = 0
    numberPermut = []
    numList = []

    # Find all the cases using the permutations module by the given numbers
    for length in range(1, len(numbers) + 1):
        numberPermut.extend(list(permutations(numbers, length)))

    # Remove duplicates using set() and find all the valid numbers
    for numInCase in set(numberPermut):
        num = int("".join(map(str, numInCase)))
        if num == 0 or num == 1:
            continue
        numList.append(num)

    # Lastly, find the counts of the prime numbers
    for num in set(numList):
        answer += 1 if isPrime(num) else 0

    return answer
