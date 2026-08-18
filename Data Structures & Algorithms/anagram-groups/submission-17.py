class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table={}
        output=[]
        for s in strs:
            key=tuple(sorted(s))
            if key in table:
                table[key].append(s)
            else:
                table[key]=[s]
        return list(table.values())
        
        