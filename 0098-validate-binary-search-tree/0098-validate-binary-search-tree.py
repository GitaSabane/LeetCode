# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # def __init__(self):
    #     # self.valid = True
    #     self.inord = []

    # def inorder(self, root):
    #     if root == None:
    #         return 

    #     self.inorder(root.left)
    #     self.inord.append(root.val)
    #     self.inorder(root.right)

    def check(self, root, mn, mx):
        if root == None:
            return True
        if root.val < mn or root.val > mx:
            return False

        checkLeft = self.check(root.left, mn, root.val-1)
        checkRight = self.check(root.right, root.val+1, mx)

        return checkLeft and checkRight
         

    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        return self.check(root, -10000000000000, 1000000000000)
        # self.inorder(root)

        # return self.inord == sorted(self.inord)



        # if root == None:
        #     return 

        # if root.left:
        #     self.isValidBST(root.left)
        #     if root.left.val >= root.val:
        #         self.valid = False

        # if root.right:
        #     self.isValidBST(root.right)
        #     if root.right.val <= root.val:
        #         self.valid = False

        # return self.valid
        