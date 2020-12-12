

def remove_dups(list):
    uniqueValues = set()
    prev = None

    for node in list:
        if node.value in uniqueValues:
            prev.next = node.next
        else:
            uniqueValues.add(node.value)
            prev = node

    return list
