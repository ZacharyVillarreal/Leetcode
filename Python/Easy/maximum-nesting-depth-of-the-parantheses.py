class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        m = 0
        
        for char in s:
            if char == "(":
                count += 1
                m = max(m, count)
            if char == ")":
                count -= 1
        return m