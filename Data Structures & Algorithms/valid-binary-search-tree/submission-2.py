# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def BSTRecCheck(self, root: Optional[TreeNode], lesser: int, greater: int) -> bool:
        if not root:
            return True
        if (lesser == 1000000001 or root.val < lesser) and (greater == 1000000001 or root.val > greater):
            return self.BSTRecCheck(root.left, root.val, greater) and self.BSTRecCheck(root.right, lesser, root.val)
        else:
            return False


    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        return self.BSTRecCheck(root.left, root.val, 1000000001) and self.BSTRecCheck(root.right, 1000000001, root.val)