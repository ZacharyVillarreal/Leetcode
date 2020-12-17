class Solution:
    def fib(self, n: int) -> int:
        start = [0, 1]
        
        if n <= 1:
            return n
            
        for i in range(2, n+1):
            start.append(start[i - 2] + start[i - 1])
            
        return start[-1]