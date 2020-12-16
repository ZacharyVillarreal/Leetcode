class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        str_1 = list(A[0])
        
        for word in A:
            new_str = []
            for char in word:
                if char in str_1:
                    new_str.append(char)
                    str_1.remove(char)
            str_1 = new_str
            
        return str_1