class Solution:
    def isPalindrome(self, str: str) -> bool:
        def is_alphanumeric(x: int) -> bool:
            # return str[x].lower() in string.ascii_lowercase or str[x] in string.digits
            return (ord('a') <= ord(str[x].lower()) <= ord('z')) or (ord('0') <= ord(str[x]) <= ord('9'))
        x = 0
        y = len(str)-1
        while x <= y:
            while x <= y and not is_alphanumeric(x):
                x += 1
            while y > 0 and not is_alphanumeric(y):
                y -= 1
            if x >= len(str) or y < 0:
                return True
            if str[x].lower() != str[y].lower():
                return False
            x += 1
            y -= 1
            
        return True