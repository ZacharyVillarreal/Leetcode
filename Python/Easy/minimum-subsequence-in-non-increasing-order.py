class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums = sorted(nums, reverse=True)
        total = sum(nums)
        
        for i in range(1, len(nums) + 1):
            partial_sum = sum(nums[:i])
            
            if total - partial_sum < partial_sum:
                return nums[:i]
        
        