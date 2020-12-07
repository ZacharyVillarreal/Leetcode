class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        success = 0
        times = zip(startTime, endTime)
        
        for i in times:
            if queryTime in range(i[0], i[1]+1):
                success += 1
                
        return success