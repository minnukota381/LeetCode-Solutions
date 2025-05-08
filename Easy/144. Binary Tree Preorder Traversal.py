# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        r=[]
        self.preorder(root,r)
        return r

    def preorder(self,root,r):
        if root is None:
            return
        r.append(root.val)
        self.preorder(root.left,r)
        self.preorder(root.right,r)