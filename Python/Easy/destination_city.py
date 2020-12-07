class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        pairs = {}
        
        for i in paths:
            pairs[i[0]] = i[1]
        
        for k, v in paths:
            if v not in pairs:
                return v
            