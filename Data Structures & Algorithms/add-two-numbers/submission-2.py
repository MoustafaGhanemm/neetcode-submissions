# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        

        prev = l1
        carry = 0
        while l1 and l2:
            total = l1.val + l2.val + carry

            carry = total // 10
            l1.val = total % 10

            
            prevl1 = l1
            prevl2 = l2
            l1 = l1.next
            l2 = l2.next
        if l2:                   # l2 is longer: splice its leftovers on
            prevl1.next = l2
        curr = prevl1.next       # leftover chain (or None)
        last = prevl1
        while carry:
            if not curr:         # ran out of nodes: add one for the carry
                last.next = ListNode(carry)
                break
            total = curr.val + carry
            carry = total // 10
            curr.val = total % 10
            last = curr
            curr = curr.next
        return prev
        




