# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        s,f=head,head.next

        while f and f.next:
            s=s.next
            f=f.next.next

        snd=s.next
        prev=s.next=None

        while snd:
            tmp=snd.next
            snd.next=prev
            prev=snd
            snd=tmp

        fst,snd=head,prev

        while snd:
            t1,t2 = fst.next, snd.next
            fst.next=snd
            snd.next=t1
            fst,snd=t1,t2
            
        
