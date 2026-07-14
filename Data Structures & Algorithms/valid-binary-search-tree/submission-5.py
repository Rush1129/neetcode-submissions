# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        l = []
        if not root:
            return True

        def inorder(node):
            if not node:
                return False      
            
            inorder(node.left)
            l.append(node.val)
            inorder(node.right)

        def isSorted(l):
            pre = l[0]
            for i in range(1,len(l)):
                if l[i]<=pre:
                    return False
                pre=l[i]
            return True

        inorder(root)
        return isSorted(l)