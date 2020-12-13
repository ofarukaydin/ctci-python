class Node:
    def __init__(self, value, left=None, right=None):
        self.right = right
        self.left = left
        self.value = value


def is_valid_bst(node, min=float("-inf"), max=float("inf")):
    if not node:
        return True

    if node.value <= min or node.value > max:
        return False

    if not is_valid_bst(node.left, min, node.value) or not is_valid_bst(node.right, node.value, max):
        return False

    return True


tree = Node(20, Node(15, Node(10), Node(16)),
            Node(22, Node(21), Node(23)))

print(is_valid_bst(tree))
