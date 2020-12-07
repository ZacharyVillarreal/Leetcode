class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        evens = []
        odds = []
        
        for i in A:
            if i % 2 == 1:
                odds.append(i)
            else:
                evens.append(i)
        return evens + odds