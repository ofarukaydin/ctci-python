

def intersect(list1, list2):
    if list1[-1] != list2[-1]:
        return None
    else:
        longerList, smallerList = (list1, list2) if len(
            list1) > len(list2) else (list2, list1)
        offset = abs(len(list1) - len(list2))

        for i in range(len(smallerList)):
            if (smallerList[i] == longerList[i + offset]):
                return smallerList[i]

    return None
