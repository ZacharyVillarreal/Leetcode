class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        cur = 0
        
        for i in s:
            if i == 'L':
                cur += 1
            if i == 'R':
                cur -= 1
            if cur == 0:
                count += 1
        
        return count