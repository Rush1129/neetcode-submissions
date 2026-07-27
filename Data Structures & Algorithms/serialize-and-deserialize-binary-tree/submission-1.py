# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        if not root:
            return ''

        res = []
        q = deque([root])

        while q:
            cur = q.popleft()
            if cur=='N':
                res.append('N')
                continue

            res.append(f'{cur.val}')

            if cur.left:
                q.append(cur.left)
            else:
                q.append('N')

            if cur.right:
                q.append(cur.right)
            else:
                q.append('N')

        return ','.join(res)
     
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        if len(data)==0:
            return None
        ldata = data.split(',')

        root = TreeNode(ldata[0])
        q = deque([root])
        i=1
        while i<len(ldata):
            cur = q.popleft()
            if ldata[i]!='N':
                l = TreeNode(ldata[i])
                cur.left = l
                q.append(l)
            i+=1 
            if ldata[i]!='N':
                r = TreeNode(ldata[i])
                cur.right = r
                q.append(r)
            i+=1
        return root