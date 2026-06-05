# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        ans1,ans2=False,False
        def subdfs(node,snode):
            if not node and not snode:
                return True
            if not node or not snode:
                return False
            if node.val!=snode.val:
                return False
            return subdfs(node.left,snode.left) and subdfs(node.right,snode.right)

        if not root:
            return False
        if not subRoot:
            return True

        if subdfs(root,subRoot):
            return True
    
        ans1=self.isSubtree(root.left,subRoot)
        ans2=self.isSubtree(root.right,subRoot)
    
        return ans1 or ans2