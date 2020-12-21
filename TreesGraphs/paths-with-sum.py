# TODO implement more efficent algorithm


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


def count_path_with_sum(root, targetSum):
    if not root:
        return 0

    pathsFromRoot = count_paths_with_sum_from_node(root, targetSum, 0)

    pathsOnLeft = count_path_with_sum(root.left, targetSum)
    pathsOnRight = count_path_with_sum(root.right, targetSum)

    return pathsFromRoot + pathsOnLeft + pathsOnRight


def count_paths_with_sum_from_node(node, targetSum, currentSum):
    if not node:
        return 0

    currentSum += node.val

    totalPaths = 0

    if currentSum == targetSum:
        totalPaths += 1

    totalPaths += count_paths_with_sum_from_node(
        node.left, targetSum, currentSum)
    totalPaths += count_paths_with_sum_from_node(
        node.right, targetSum, currentSum)

    return totalPaths


tree = Node(1, Node(5, Node(4, Node(-10), Node(7)), Node(-2)),
            Node(3, Node(-4, Node(1), Node(2)), Node(-8, Node(-7), Node(-10))))

count_path_with_sum(tree, 0)
