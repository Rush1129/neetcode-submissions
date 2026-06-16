# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
            if not lists or len(lists)==0:
                return None
            r = 1
            head = ListNode(0)
            l = lists[0]
            while r<len(lists):
                h=head     
                f = l
                s = lists[r]

                while f and s:
                    if f.val<=s.val:
                        h.next=f
                        f=f.next
                    else:
                        h.next=s
                        s=s.next
                    h=h.next 
                h.next = f or s
                l=head.next
                r+=1
            return head.next

