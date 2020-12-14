import collections

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        ans = collections.Counter()
        
        for i in cpdomains:
            n, i = i.split()
            ans[i] += int(n)
            
            for j in range(len(i)):
                if i[j] == '.':
                    ans[i[j + 1:]] += int(n)
        
        return ["{} {}".format(ans[k], k) for k in ans]