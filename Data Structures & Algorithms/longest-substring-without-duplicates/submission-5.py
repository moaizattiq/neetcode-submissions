class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        longest=0
        windowset=set()
        for r in range (len(s)):
            while s[r] in windowset:
                windowset.remove(s[l])
                l += 1
            windowset.add(s[r])
            window = (r-l) + 1
            longest = max (window,longest)
        return longest
        