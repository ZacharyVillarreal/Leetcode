class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        counts = [0] * 61
        val = 0
        
        for i in range(len(time)):
            x = time[i] % 60
            val += counts[60 - x]
            if x == 0:
                counts[60] += 1
            else:
                counts[x] += 1
        return val