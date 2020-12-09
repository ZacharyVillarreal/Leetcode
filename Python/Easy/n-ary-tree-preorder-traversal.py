"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        lst = []
        if root == None:
            return lst
        stack = [root]
        while stack:
            current = stack.pop()
            lst.append(current.val)
            stack.extend(current.children[::-1])
            
        return lst
        