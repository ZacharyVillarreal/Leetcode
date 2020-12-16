class Solution:
    def average(self, salary: List[int]) -> float:
        min_ = min(salary)
        max_ = max(salary)
        sum_ = sum(salary)
                
        return (sum_ - min_ - max_) / (len(salary) - 2)