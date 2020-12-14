class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        self.df(s, [], res)
        return res
    
    def df(self, s, path, res):
        if not s:
            res.append(path)
            return
    
        for i in range(1, len(s) + 1):
            if self.palindrome(s[:i]):
                self.df(s[i:], path + [s[:i]], res)
    
    def palindrome(self, s):
        return s == s[::-1]
    