class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        min_ = {min(i) for i in matrix}
        max_ = {max(i) for i in zip(*matrix)}
        
        return list(min_ & max_)
    