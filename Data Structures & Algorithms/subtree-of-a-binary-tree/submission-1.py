# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        
        def IST(p,q):
            if not p and not q:
                return True
            elif not p and q:
                return False
            elif p and not q:
                return False

            if p.val == q.val:
                return IST(p.right, q.right) and IST(p.left, q.left)
            else:
                return False
        
        if not root and not subRoot:
            return True
        elif not root and subRoot:
            return False
        elif root and not subRoot:
            return True
        
        
        return (IST(root, subRoot)
        or self.isSubtree(root.left, subRoot)
        or self.isSubtree(root.right, subRoot))
            



