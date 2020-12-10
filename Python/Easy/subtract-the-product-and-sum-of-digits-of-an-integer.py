import numpy as np
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        return np.prod([int(i) for i in str(n)]) - np.sum([int(i) for i in str(n)])