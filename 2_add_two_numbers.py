from typing import Optional

# This class needs to be commented to submmit in Leetcode
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


def convertToNumber(node: ListNode) -> int:
    numerals = []
    while node:
        numerals.append(str(node.val))
        node = node.next

    numerals.reverse()
    return int(''.join(numerals))


def showNumber(node: ListNode):
    while node:
        if node:
            print(node.val, end='')
        node = node.next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = convertToNumber(l1)
        n2 = convertToNumber(l2)
        sum = n1 + n2
        number = list(str(sum))
        current_node = ListNode(val=int(number[0]))

        for n in number[1:]:
            current_node = ListNode(val=int(n), next=current_node)
        return current_node
