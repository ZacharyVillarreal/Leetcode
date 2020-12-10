class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans = [''] * len(s)
        for i, char in zip(indices, s):
            ans[i] = char
    
        return "".join(ans)
            
            