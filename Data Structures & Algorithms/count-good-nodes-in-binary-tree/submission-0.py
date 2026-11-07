# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodSearch(self, curr: TreeNode, maxInPath: int) -> int:
        if not curr:
            return 0
        sol = 0
        if curr.val >= maxInPath:
            sol = 1
        return sol + self.goodSearch(curr.left,max(curr.val,maxInPath)) + self.goodSearch(curr.right,max(curr.val,maxInPath))

    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        return 1 + self.goodSearch(root.left,root.val) + self.goodSearch(root.right,root.val)
        