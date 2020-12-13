class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        ans = []
        num = 0
        
        for i in arr:
            if i >= num:
                num = i
                ans.append(i)
            else:
                break
        
        return ans.index(max(ans))