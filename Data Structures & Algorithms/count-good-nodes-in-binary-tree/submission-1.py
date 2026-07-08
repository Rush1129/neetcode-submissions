# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        maxx = float('-inf')
        n=0
        def dfs(node,maxx):
            nonlocal n
            if not node: return

            if node.val>=maxx:
                n+=1
                maxx=node.val
            
            dfs(node.left,maxx)
            dfs(node.right,maxx)
        dfs(root,maxx)

        return n