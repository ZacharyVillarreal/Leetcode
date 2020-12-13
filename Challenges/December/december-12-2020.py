# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        def subtree(node):
            if not node:
                return [0, None]
            
            l_d, l_res = subtree(node.left)
            r_d, r_res = subtree(node.right)
            res = [node, -1]
            
            if (l_d == 0 and r_d == 0) or (l_d == r_d):
                res = node
            else:
                res = l_res if l_d > r_d else r_res
            
            return [max(l_d, r_d) + 1, res]
    
        d, res = subtree(root)
        return res