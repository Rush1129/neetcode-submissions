# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p=head
        l=0
        while p!=None:
            l+=1
            p=p.next

        p=head
        q=head
        if l==n:
            return head.next

        while p!=None:
            p=p.next
            l-=1
            if l==n:
                q.next=p.next
            if q.next:
                q=q.next
              
        return head