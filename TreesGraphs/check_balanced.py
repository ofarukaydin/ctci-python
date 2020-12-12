class Node:
    def __init__(self, val, left=None, right=None):
        self.right = right
        self.left = left
        self.val = val

    def __str__(self):
        return (
            "("
            + str(self.left)
            + ":L "
            + "V:"
            + str(self.val)
            + " R:"
            + str(self.right)
            + ")"
        )

    def element(self):
        return self.val


def calculateHeight(node):
    if not node:
        return (0, True)

    h1, isLeftBalanced = calculateHeight(node.left)
    h2, isRightBalanced = calculateHeight(node.right)

    height = h1 + 1 if h1 > h2 else h2 + 1

    if abs(h1 - h2) > 1 or not isLeftBalanced or not isRightBalanced:
        return (height, False)
    else:
        return (height, True)


tree = Node(0, Node(1, Node(3, Node(6), Node(10, Node(20))), Node(
    7, Node(11), Node(12))), Node(2, Node(5), Node(4)))

print(calculateHeight(tree))
