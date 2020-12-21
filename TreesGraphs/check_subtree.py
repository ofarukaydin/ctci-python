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


def preorder(root, results):
    if not root:
        results.append('X')
        return

    results.append(str(root.val))
    preorder(root.left, results)
    preorder(root.right, results)


def check_is_subtree(t1, t2):
    preorder1 = []
    preorder2 = []

    preorder(t1, preorder1)
    preorder(t2, preorder2)

    preorder1_string = "".join(preorder1)
    preorder2_string = "".join(preorder2)

    return preorder1_string.find(preorder2_string) != -1


tree = Node(2, Node(5, Node(7), Node(8)), Node(6, None, Node(11)))
subtree = Node(6, None, Node(11))

print(check_is_subtree(tree, subtree))
