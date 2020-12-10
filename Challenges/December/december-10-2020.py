class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) <= 2 or arr[0] >= arr[1]:
            return False
    
        up = True
        
        for i in range(len(arr) - 1):
            if up:
                if arr[i + 1] <= arr[i]:
                    up = False
            if not up:
                if arr[i + 1] >= arr[i]:
                    return False
        return not up
            