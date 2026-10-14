# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        



        if not head:
            return head
        st = head
        length = 0
        while st:
            length += 1
            st = st.next

        k = k % length          # added
        if k == 0:              # added
            return head         # added

        k_len = length - k
        k_head = head
        while k_len !=0:
            k_len -= 1
            if k_len == 0:
                break
            k_head = k_head.next
        
        
        second = k_head.next
        dummy = second
        k_head.next = None

    
    
        while second.next:          # added
            second = second.next    # added
        second.next = head          # added
        
        return dummy
        


        



        

        
