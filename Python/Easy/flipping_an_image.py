class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        ans = []
        
        for i in A:
            row = []
            for j in i[::-1]:
                if j == 1:
                    row.append(0)
                else:
                    row.append(1)
            ans.append(row)
            
        return ans