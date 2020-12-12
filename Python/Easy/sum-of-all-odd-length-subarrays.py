class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        len_ = len(arr)
        sum_ = 0
        
        for i in range(1, len_ + 1, 2):
            for j in range(len_ - i + 1):
                sum_ += sum(arr[j : i + j])
                
        return sum_