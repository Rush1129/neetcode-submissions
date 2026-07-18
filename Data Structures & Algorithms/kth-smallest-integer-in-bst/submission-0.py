# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    
        cnt=0
        ans=0
        def dfs(node):
            nonlocal cnt
            if not node:
                return 0

            dfs(node.left)
            cnt+=1
            if cnt==k:
                nonlocal ans
                ans=node.val
            dfs(node.right)

        dfs(root)
        return ans



