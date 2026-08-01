from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdict=defaultdict(int)
        for c in s:
            sdict[c] += 1
        tdict=defaultdict(int)
        for c in t:
            tdict[c] += 1
        if sdict == tdict:
            return True
        return False
        