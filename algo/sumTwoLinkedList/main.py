from typing import List


class ListNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def genLinkedListFromArray(array):
    node = ListNode()
    head = node
    for i in range(0, len(array)):
        node.val = array[i]

        if (i == len(array) - 1):
            node.next = None
        else:
            node.next = ListNode()

        node = node.next

    return head


def sumTwoLinkedList(l1, l2):
    head = l3 = ListNode(0)
    carry = 0

    while l1 or l2 or carry:
        if l1:
            carry += l1.val
            l1 = l1.next
        if l2:
            carry += l2.val
            l2 = l2.next

        l3.val = carry % 10
        carry = carry // 10

        if l1 or l2 or carry:
            l3.next = ListNode(0)
            l3 = l3.next

    return head


if __name__ == '__main__':
    l1 = genLinkedListFromArray([2, 4, 3])
    l2 = genLinkedListFromArray([5, 6, 4])
    r = sumTwoLinkedList(l1, l2)
