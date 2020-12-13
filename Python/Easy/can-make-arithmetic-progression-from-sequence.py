class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        if len(arr) <= 1:
            return True
    
        arr.sort()
        diff = arr[1] - arr[0]
        
        return all(diff == arr[i + 1] - arr[i] for i in range(1, len(arr)-1))