class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        d = {}
        
        for i in A:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        
        for k, v in d.items():
            if v == len(A) / 2:
                return k