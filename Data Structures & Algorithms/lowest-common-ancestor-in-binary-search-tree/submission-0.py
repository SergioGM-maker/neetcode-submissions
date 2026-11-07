# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def ancestryPath(self, root: TreeNode, x: TreeNode, sol: List[TreeNode]) -> None:
        sol.append(root)
        if root.val < x.val:
            self.ancestryPath(root.right,x,sol)
        elif root.val > x.val:
            self.ancestryPath(root.left,x,sol)



    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        p_path = []
        self.ancestryPath(root,p,p_path)
        q_path = []
        self.ancestryPath(root,q,q_path)
        i = 0
        sol = root
        while i < len(q_path) and i < len(p_path) and q_path[i] == p_path[i]:
            sol = p_path[i]
            i+= 1
        return sol
        