class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        d = { piece[0]: piece for piece in pieces}
        ans = []
        
        for i in arr:
            ans += d.get(i, [])
        
        return ans == arr