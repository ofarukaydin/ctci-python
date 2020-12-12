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
