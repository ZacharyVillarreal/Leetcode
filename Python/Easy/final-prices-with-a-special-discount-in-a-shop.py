class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        len_ = len(prices)
        i = 0
        
        while i <= len_ - 2:
            for j in range(i+1, len(prices)):
                if prices[i] >= prices[j]:
                    prices[i] -= prices[j]
                    break
            i += 1
        
        return prices