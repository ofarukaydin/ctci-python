from LinkedLists.LinkedList import LinkedList

from TreesGraphs.Node import Node


def get_depth(root):
    levels = []
    current = LinkedList()
    if root:
        current.push_wrapped(root)

    while len(current) > 0:
        levels.append(current)
        parents = current
        current = LinkedList()
        for node in parents:
            if node.value.left:
                current.push_wrapped(node.value.left)
            if node.value.right:
                current.push_wrapped(node.value.right)
    return levels


tree = Node(0, Node(1, Node(3, Node(6), Node(10)), Node(
    7, Node(11), Node(12))), Node(2, Node(5), Node(4)))


depth_lists = get_depth(tree)
depth = len(depth_lists)
print(depth)
for level in depth_lists:
    for node in level:
        # First unwrap from LinkedList Node then unwrap from Tree Node
        print(node.element().element())
