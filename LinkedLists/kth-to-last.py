from .LinkedList import LinkedList


def kth_to_last(head, k):
    pt1 = pt2 = head
    for i in range(k):
        pt1 = pt1.next

    while pt1 and pt2:
        pt1 = pt1.next
        pt2 = pt2.next
    return pt2.value


list = LinkedList(1, 2, 3, 4, 5)
