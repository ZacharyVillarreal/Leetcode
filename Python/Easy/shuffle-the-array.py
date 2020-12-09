class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        return[item for t in zip(nums[:n+1], nums[n:]) for item in t] 