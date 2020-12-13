class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        even_count = 0
        odd_count = 0
        
        for i in position:
            if i % 2 == 1:
                odd_count += 1
            else:
                even_count += 1
        
        return min(odd_count, even_count)