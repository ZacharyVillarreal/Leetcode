# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode, tail=None) -> TreeNode:
        if not root:
            return tail
        x = TreeNode(root.val)
        x.right = self.increasingBST(root.right, tail)
        return self.increasingBST(root.left, x)