# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        def dfs(node,p):
            if not node:
                if val<p.val:
                    p.left=TreeNode(val)
                    return
                if val>p.val:
                    p.right=TreeNode(val)
                    return                    
            
            if node.val<val:
                dfs(node.right, node)
            elif node.val>val:
                dfs(node.left, node)

        dfs(root,0)
        return root