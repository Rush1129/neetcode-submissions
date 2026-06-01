"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        cdic = {None:None}

        h=head
        while h:
            copy = Node(h.val)
            cdic[h]=copy
            h=h.next

        h=head
        while h:
            cdic[h].next = cdic[h.next]
            cdic[h].random = cdic[h.random]
            h = h.next
        
        return cdic[head]
