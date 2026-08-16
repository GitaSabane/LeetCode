# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.s = set()

    def inOrder(self, root):
        if root == None:
            return 
        self.inOrder(root.left)
        self.s.add(root.val)
        self.inOrder(root.right)

    def findSecondMinimumValue(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        self.inOrder(root)

        if len(self.s) < 2:
            return -1
        return sorted(self.s)[1]
        