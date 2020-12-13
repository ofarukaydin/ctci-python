
import unittest


def successor(node):
    if node.right:
        current = node.right
        if not current.left:
            return current
        else:
            while current.left:
                current = current.left
            return current
    else:
        parent = node.parent
        while parent and node.data > parent.data:
            parent = parent.parent
        return parent


class Node():
    def __init__(self, data, left=None, right=None):
        self.data, self.left, self.right = data, left, right
        self.parent = None
        if self.left:
            self.left.parent = self
        if self.right:
            self.right.parent = self


class Test(unittest.TestCase):
    def test_successor(self):
        self.assertEqual(successor(Node(22, Node(11))), None)
        self.assertEqual(successor(Node(22, Node(11), Node(33))).data, 33)
        self.assertEqual(
            successor(Node(22, Node(11), Node(33, Node(28)))).data, 28)
        self.assertEqual(successor(Node(22, Node(11), Node(33)).left).data, 22)
        self.assertEqual(successor(Node(22, Node(11), Node(33)).right), None)


if __name__ == "__main__":
    unittest.main()
