class Number:
    def __init__(self, order, operator, number):
        # The order of the numbers
        self.order = order

        # The value "True" indicates this number is positive
        # Oppositely, if the value is "False" then the number will be negative
        self.operator = operator

        # The given number
        self.number = number

        # Is this number visited?
        self.visited = False


def dfs(numberList, node, current):
    global globalAnswer
    global globalLength
    global globalTarget

    node.visited = True

    # Calculate the current sum of numbers so far
    current += node.number if node.operator else -node.number

    if node.order == globalLength - 1:
        # If the current node is the last number of its number sequence
        globalAnswer += 1 if current == globalTarget else 0

    for number in numberList:
        if number.order == node.order + 1 and not number.visited:
            # Go through to the next order number
            dfs(numberList, number, current)
            # Restore the visited property to make this number usable again
            number.visited = False


def solution(numbers, target):
    # Declare the global variables
    global globalAnswer
    global globalLength
    global globalTarget

    globalAnswer = 0
    globalLength = len(numbers)
    globalTarget = target

    # Init the Number instance list
    numberList = []
    for order, number in enumerate(numbers):
        numberList.append(Number(order, True, number))
        numberList.append(Number(order, False, number))

    dfs(numberList, numberList[0], 0)  # Start with first positive number
    dfs(numberList, numberList[1], 0)  # Start with first negative number

    return globalAnswer
