# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.ans = None
    def searchBST(self, root, data):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """

        if root == None:
            return None

        if root.val == data:
            return root
        if data < root.val:
            return self.searchBST(root.left, data)
        else:
            return self.searchBST(root.right, data)

        


        