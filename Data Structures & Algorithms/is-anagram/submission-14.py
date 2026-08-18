class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sets={}
        sett={}
        for c in s:
            sets[c]=sets.get(c,0)+1
        for c in t:
            sett[c]=sett.get(c,0)+1
        if sets != sett:
            return False
        return True


        