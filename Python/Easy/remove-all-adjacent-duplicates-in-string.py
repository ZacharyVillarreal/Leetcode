class Solution:
    def removeDuplicates(self, S: str) -> str:
        lst = []
        
        for char in S:
            if lst and lst[-1] == char:
                lst.pop()
            else:
                lst.append(char)
            
        return "".join(lst)