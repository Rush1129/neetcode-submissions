# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        rvis = [root.val]
        maxl=1
        def dfs(node,l):
            nonlocal maxl
            if not node:
                return
            l+=1
            if maxl<l:
                rvis.append(node.val)
                maxl+=1
            dfs(node.right,l)
            dfs(node.left,l)
        dfs(root,0)
        return rvis