from .Node import Node


def construct_binary_tree(array):
    return minimal_tree(array, 0, len(array) - 1)


def minimal_tree(array, start, end):
    if start > end:
        return ''

    mid = (start + end) // 2

    root = Node(array[mid])
    root.left = minimal_tree(array, start, mid - 1)
    root.right = minimal_tree(array, mid + 1, end)

    return root


testArray = [0, 1, 2, 3, 4, 5, 6, 7, 8]
print(construct_binary_tree(testArray))
