# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head==None:
            return False 
        s = f = head
        while(s.next!=None and f.next!=None):
            s = s.next
            if f.next.next!=None:
                f = f.next.next
            else:
                return False

            if s==f:
                return True
        return False