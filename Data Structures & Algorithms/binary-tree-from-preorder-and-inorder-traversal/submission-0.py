# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        h = {v:i for i,v in enumerate(inorder)}
        self.pre_idx=0

        def dfs(l,r):
            if l>r:
                return None

            root_val = preorder[self.pre_idx]
            self.pre_idx+=1

            t = TreeNode(root_val)
            ind = h[root_val]

            t.left = dfs(l,ind-1)
            t.right = dfs(ind+1,r)

            return t

        return dfs(0,len(inorder)-1)
