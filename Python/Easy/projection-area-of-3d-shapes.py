class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        top = sum([1 for g in grid for i in g if i > 0])
        front = sum([max(g) for g in grid])
        side = sum([max(g) for g in zip(*grid)])
        
        return top + front + side