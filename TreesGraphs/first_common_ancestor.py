def lowest_common_ancestor(curr, node1, node2):
    if (curr == None):
        return None
    elif(curr == node1 or curr == node2):
        return curr

    left_subtree = lowest_common_ancestor(curr.left, node1, node2)
    right_subtree = lowest_common_ancestor(curr.right, node1, node2)

    if(left_subtree != None and right_subtree != None):
        return curr
    elif(left_subtree != None):
        return left_subtree
    else:
        return right_subtree
