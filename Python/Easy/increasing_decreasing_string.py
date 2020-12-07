class Solution:
    def sortString(self, s: str) -> str:
        lst = list(s) 
        ans = ""
        
        while lst:
            for i in sorted(set(lst)):
                lst.remove(i)
                ans += i
            for i in sorted(set(lst), reverse=True):
                lst.remove(i)
                ans += i
        
        return ans
            