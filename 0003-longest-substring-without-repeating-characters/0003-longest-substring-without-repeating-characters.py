class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = deque()
        max_substring = 0
        
        for char in s:
            while char in substring:
                substring.popleft() # remove duplicate on left window
            substring.append(char)
            max_substring = max(max_substring, len(substring))
            
        return max_substring
