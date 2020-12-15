class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        soldiers = [(sum(mat[i]), i) for i in range(len(mat))]
        soldiers = sorted(soldiers)
        ans = [num for (i, num) in soldiers]
        return ans[:k]
        

        