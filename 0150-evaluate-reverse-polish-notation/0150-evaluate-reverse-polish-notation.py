class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # truncate to 0
        # always use ints
        # no div/0
        operations = {
            "+": lambda x,y: x+y, 
            "-": lambda x,y: x-y, 
            "*": lambda x,y: x*y, 
            "/": lambda x,y: int(x/y), 
        }
        stack = []
        for token in tokens:
            # print(stack)
            if token in operations:
                b = stack.pop()
                a = stack.pop()
                stack.append(operations[token](a, b))
            else:
                stack.append(int(token))
        return stack[0]