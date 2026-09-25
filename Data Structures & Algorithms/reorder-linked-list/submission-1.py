# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #get length

        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        
        sec_half = slow.next
        slow.next = None

        prev = None
        temp = sec_half
        while temp:
            nxt = temp.next
            temp.next = prev
            prev = temp
            temp = nxt
        dummy = ListNode()
        tail = dummy

        while prev and head:
            tail.next = head
            tail = tail.next
            head = head.next

            tail.next = prev
            tail = tail.next
            prev = prev.next

        tail.next = head




        

