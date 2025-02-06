# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        r=[]
        self.inorder(root,r)
        return r
    
    def inorder(self,root,r):
        if root is None:
            return
        self.inorder(root.left,r)
        r.append(root.val)
        self.inorder(root.right,r)
        