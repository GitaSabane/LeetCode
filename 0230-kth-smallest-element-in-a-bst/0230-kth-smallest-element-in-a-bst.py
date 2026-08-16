# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.l = []
    def inOrder(self, root):
        if root == None:
            return 
        self.inOrder(root.left)
        self.l.append(root.val)
        self.inOrder(root.right)
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        self.inOrder(root)

        return self.l[k - 1]


        