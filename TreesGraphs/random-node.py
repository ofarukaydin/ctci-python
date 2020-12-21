from random import randint


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
  
# This is used to fill children counts.  
def getElements(root):  
  
    if root == None:  
        return 0
          
    return (getElements(root.left) +
            getElements(root.right) + 1)  
  
# Inserts Children count for each node  
def insertChildrenCount(root):  
  
    if root == None: 
        return
  
    root.children = getElements(root) - 1
    insertChildrenCount(root.left)  
    insertChildrenCount(root.right)  
  
# Returns number of children for root  
def children(root): 
  
    if root == None:  
        return 0
    return root.children + 1
  
# Helper Function to return a random node  
def randomNodeUtil(root, count):  
  
    if root == None:  
        return 0
  
    if count == children(root.left):  
        return root.val  
  
    if count < children(root.left):  
        return randomNodeUtil(root.left, count)  
  
    return randomNodeUtil(root.right,  
            count - children(root.left) - 1)  
  
# Returns Random node  
def randomNode(root):  
  
    count = randint(0, root.children)  
    return randomNodeUtil(root, count) 
