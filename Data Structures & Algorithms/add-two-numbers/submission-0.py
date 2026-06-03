# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p=l1
        n1=0
        c=1
        while p:
            n1+=p.val*c
            c*=10
            p=p.next
        n2=0
        c=1
        p=l2
        while p:
            n2+=p.val*c
            c*=10
            p=p.next

        ans=n1+n2
        lans=ListNode(ans%10)
        head=lans
        p=lans
        ans//=10
        while ans!=0:
            lans=ListNode(ans%10)
            p.next=lans
            p=p.next
            ans//=10
        return head