class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        ans = []
        distances = []
        
        for r in range(R):
            for c in range(C):
                distances.append([abs(r - r0) + abs(c - c0)])
                ans.append([r, c])
                
        dist, ans = zip(*sorted(zip(distances, ans)))
        
        return ans
                