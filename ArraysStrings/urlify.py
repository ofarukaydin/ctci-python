def urlify(string):
    charArray = [i for i in string]
    for i in range(len(charArray)):
        if charArray[i] == ' ':
            charArray[i] = '%20'
    return ''.join(charArray)


def urlify2(string):
    return string.strip().replace(" ", "%20")
