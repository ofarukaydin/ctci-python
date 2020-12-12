from .LinkedList import LinkedList


def sum_lists(list1, list2):
    pt1 = list1[0]
    pt2 = list2[0]
    carry = 0
    linkedList = LinkedList()
    while pt1 or pt2:
        sum = (pt1.value if pt1 else 0) + (pt2.value if pt2 else 0) + carry
        digit = sum % 10
        carry = sum // 10
        linkedList.push(digit)
        if pt1:
            pt1 = pt1.next
        if pt2:
            pt2 = pt2.next
    if carry:
        linkedList.push(carry)
    return linkedList


sum_lists(LinkedList(9, 7, 8, 9, 8), LinkedList(6, 8, 5))
