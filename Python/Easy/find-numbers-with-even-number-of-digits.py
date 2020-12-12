class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        num_len = [len(str(i)) for i in nums]
        count = 0
        
        for i in num_len:
            if i % 2 == 0:
                count += 1
        
        return count

        return sum([len(str(i)) % 2 == 0 for i in nums])