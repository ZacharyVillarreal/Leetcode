class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        z = x ^ y
        bits = 0
        
        while z > 0:
            bits += z & 1
            z >>= 1
            
        return bits