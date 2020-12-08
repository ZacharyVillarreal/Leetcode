class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        ans = []
        low = 0
        high = len(S)
        for i in S:
            if i == "I":
                ans.append(low)
                low += 1
            else:
                ans.append(high)
                high -= 1
        return ans + [low]