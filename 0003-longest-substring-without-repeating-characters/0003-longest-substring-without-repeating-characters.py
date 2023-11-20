# yoinked from neetcode
# https://youtu.be/wiGpQwVHdE0

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0
        
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l]) # remove duplicate on left window
                l += 1
            charSet.add(s[r])
            res = max(res, r-l+1)
            
        return res