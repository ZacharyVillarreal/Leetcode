import collections

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_count = collections.Counter(chars)
        ans = 0
        
        for word in words:
            word_count = collections.Counter(word)
            
            if all(chars_count[ch] >= word_count[ch] for ch in word_count):
                ans += len(word)
                
        return ans