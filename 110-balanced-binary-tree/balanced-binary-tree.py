# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.balance = True
    def depth(self, root):

        if root == None:
            return 0

        leftd = self.depth(root.left)
        rightd = self.depth(root.right)

        if abs(leftd - rightd) > 1:
            self.balance = False
        return max(leftd, rightd) + 1

    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        self.depth(root)

        return self.balance
        