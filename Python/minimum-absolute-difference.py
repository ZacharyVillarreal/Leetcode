class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        ans = []
        min_ = math.inf
        d = collections.defaultdict(list)
        arr.sort()
        
        for i in range(len(arr) - 1):
            diff = arr[i + 1] - arr[i]
            d[diff].append([arr[i], arr[i + 1]])
            min_ = min(min_, diff)
            
        return d[min_]