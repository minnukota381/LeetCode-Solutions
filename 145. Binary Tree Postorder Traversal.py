# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        r=[]
        self.postorder(root,r)
        return r

    def postorder(self,root,r):
        if root is None:
            return
        self.postorder(root.left,r)            
        self.postorder(root.right,r)
        r.append(root.val)
        