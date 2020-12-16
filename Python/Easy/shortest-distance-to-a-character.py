class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        forward = []
        for i, v in enumerate(S):
            if v == C:
                forward.append(i)

        reverse = []
        for i in range(len(S)):
            reverse.append(min([abs(t - i)for t in forward]))
        
        return reverse
            