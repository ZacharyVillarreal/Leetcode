class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        even = 0
        odd = 1
        len_ = len(A)
        
        while even < len_ and odd < len_:
            if A[even] % 2 == 0:
                even += 2
            elif A[odd] % 2 == 1:
                odd += 2
            else:
                A[even], A[odd] = A[odd], A[even]
                even += 2
                odd += 2
                
        return A
        