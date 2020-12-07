class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = []
        
        #Take care of case when n is odd
        if n%2 != 0:
            ans.append(0)
        
        for i in range(1, n):
            if len(ans) == n:
                break
            else:
                ans.append(i)
                ans.append(-i)

        return ans