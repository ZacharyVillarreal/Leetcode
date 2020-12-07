class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for i in range(left, right+1):
            nums = list(str(i))
            success = 0
            for j in nums:
                if int(j) == 0:
                    continue
                if i % int(j) == 0:
                    success += 1
            if success == len(nums):
                ans.append(i)
        return ans
                    
            