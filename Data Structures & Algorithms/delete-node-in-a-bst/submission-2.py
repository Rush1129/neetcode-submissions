# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if root.val == key:
            if not root.left and not root.right:
                return None

            if not root.left:
                return root.right

            t = root.right
            
            root = root.left
            n = root
            while n.right:
                n = n.right
            n.right = t
            return root

        
        if root.val>key:
            if not root.left:
                return root
            if root.left.val == key:
                if not root.left.left and not root.left.right:
                    root.left = None
                    return root

                if not root.left.left:
                    root.left = root.left.right
                    return root

                t = root.left.right
                root.left = root.left.left
                n = root.left
                while n.right:
                    n=n.right
                n.right=t
                return root
            else:
                self.deleteNode(root.left,key)

        if root.val<key:
            if not root.right:
                return root
            if root.right.val == key:
                if not root.right.left and not root.right.right:
                    root.right = None
                    return root

                if not root.right.left:
                    root.right = root.right.right
                    return root

                t = root.right.right
                root.right = root.right.left
                n = root.right
                while n.right:
                    n=n.right
                n.right=t
                return root
            else:
                self.deleteNode(root.right,key)

        return root