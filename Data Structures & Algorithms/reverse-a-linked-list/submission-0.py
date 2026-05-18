class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        p=None
        q=head
        r=head
        while(q!=None):
            r = q.next
            q.next = p
            p = q
            q = r
        
        head = p

        return head