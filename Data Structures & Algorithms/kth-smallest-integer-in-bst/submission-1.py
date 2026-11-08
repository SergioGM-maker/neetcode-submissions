# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def searchTree(self, root: Optional[TreeNode], target: int,  count: int, solved: bool) -> tuple[int, bool]:
        if not root:
            return count, False

        sol, state = self.searchTree(root.left, target, count,  solved)

        if state:
            return sol, state
        count = sol +1

        if count == target:
            return root.val, True
        
        sol, state = self.searchTree(root.right, target, count,  solved)

        if state:
            return sol, state
        elif sol == 0:
            return count, state
        return sol, state



    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return None
        
        sol, state = self.searchTree(root, k, 0, False)

        return sol
        