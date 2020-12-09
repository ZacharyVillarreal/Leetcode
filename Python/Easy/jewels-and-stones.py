class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewels = set([i for i in J])
        count = 0
        
        for i in S:
            if i in jewels:
                count += 1
        
        return count