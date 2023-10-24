class Solution:
    def isValid(self, s: str) -> bool:
        # return early
        if len(s) % 2 != 0 or len(s) == 0:
            return False
        # lookup close brace
        closing = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        # only contains parens, brackets, and braces
        stack = []
        for c in s:
            if len(stack) > 0 and c in closing and stack[-1] == closing[c]:
                stack.pop()
            else:
                stack.append(c)
        return len(stack) == 0