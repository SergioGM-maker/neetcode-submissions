# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inputOrdered(self, curr: Optional[TreeNode], sol: List[List[int]], level: int) -> None:
        if len(sol) < level +1:
            sol.append([curr.val])
        else:
            sol[level].append(curr.val)

        if curr.left:
            self.inputOrdered(curr.left,sol,level+1)
        if curr.right:
            self.inputOrdered(curr.right,sol,level+1)


    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        sol = []
        if not root:
            return sol
        self.inputOrdered(root, sol, 0)
        
        return sol
        