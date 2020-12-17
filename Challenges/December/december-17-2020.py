class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        successes = 0
        d = {}
        
        for i in C:
            for j in D:
                s = i + j
                if s not in d:
                    d[s] = 1
                else:
                    d[s] += 1
                    
        for i in range(len(A)):
            for j in range(len(B)):
                target = 0 - (A[i] + B[j])
                if target in d:
                    successes += d[target]
                    
        return successes