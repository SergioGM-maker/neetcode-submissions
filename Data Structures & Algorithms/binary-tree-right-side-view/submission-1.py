# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def traversal(self, root: Optional[TreeNode], sol: List[int], level: int) -> None:
        if root:
            if len(sol) < level:
                sol.append(root.val)
            
            self.traversal(root.right, sol, level + 1)
            self.traversal(root.left, sol, level +1)


    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        sol = []
        if not root:
            return sol

        self.traversal(root, sol, 1)

        return sol