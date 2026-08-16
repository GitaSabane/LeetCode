# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insert(self, root, node):
        if root == None:
            root = node
            return root

        if node.val < root.val:
            if root.left == None:
                root.left = node
            else:
                self.insert(root.left,node)

        if node.val > root.val:
            if root.right == None:
                root.right = node
            else:
                self.insert(root.right,node)
        

    def insertIntoBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """

        node = TreeNode(val)
        self.insert(root, node)

        if root == None:
            root = node
            return root

        return root
            
        