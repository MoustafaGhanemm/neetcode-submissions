# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next
        end = length - n
        if end == 0:
            return head.next
        temp_len = 0
        temp2 = head
        while temp2:
            if temp_len == end - 1:
                temp2.next = temp2.next.next
                break
            temp_len += 1
            temp2 = temp2.next
        return head



