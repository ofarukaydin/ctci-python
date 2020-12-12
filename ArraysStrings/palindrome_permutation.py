from collections import Counter


def is_palindrome_permutation(input):
    counter = Counter()
    for c in input:
        if c in counter:
            counter[c] -= 1
        else:
            counter[c] += 1
    counterSum = sum(counter.values())
    if counterSum == 1 or counterSum == 0:
        return True
    else:
        return False
