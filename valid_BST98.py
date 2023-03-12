# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(root: Optional[TreeNode], min:int, max: int):
        if root is None:
            return True
        if min is not None and min>=root.val:
            return False
        if max is not None and max<= root.val:
            return False
        return Solution.traverse(root.left,min,root.val) and Solution.traverse(root.right, root.val,max)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return Solution.traverse(root,None,None)
        