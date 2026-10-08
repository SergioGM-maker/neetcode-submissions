# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def depth_search(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return max(
            self.depth_search(root.left),
            self.depth_search(root.right)
        ) +1



    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return max(
            self.depth_search(root.left)+self.depth_search(root.right),
            self.diameterOfBinaryTree(root.left),
            self.diameterOfBinaryTree(root.right))