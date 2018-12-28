# project euler problem 2


def realFib(limit, start = 0, previousNumber = 0, total = 0):
    if start >= limit:
        print(total)
        return 0    

    if start < 1:
        start = 1
        previousNumber = 0

    if start % 2 == 0:
        total += start

    realFib(limit, start + previousNumber, start, total)

realFib(4000000)

