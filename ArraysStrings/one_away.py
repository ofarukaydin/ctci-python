from collections import Counter


def one_away(input1, input2):
    lenDiff = abs(len(input2) - len(input1))

    if lenDiff > 1:
        return False

    counter = Counter()

    for c in input1:
        if c in counter:
            counter[c] -= 1
        else:
            counter[c] += 1

    for c in input2:
        if c in counter:
            counter[c] -= 1
        else:
            counter[c] += 1

    sumVal = sum(counter.values())

    if sumVal <= 2:
        return True
    else:
        return False
