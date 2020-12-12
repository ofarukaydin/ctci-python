def isUnique(chars):
    charMap = [False] * 128
    for char in chars:
        if charMap[ord(char)]:
            return False
        else:
            charMap[ord(char)] = True
    return True
