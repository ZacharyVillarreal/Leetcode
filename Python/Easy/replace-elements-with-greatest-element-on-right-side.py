class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans = [-1]
        max_num = 0
        for i in arr[::-1]:
            if max_num < i:
                max_num = i
            ans.append(max_num)
        ans.pop()
        return ans[::-1]
            
            