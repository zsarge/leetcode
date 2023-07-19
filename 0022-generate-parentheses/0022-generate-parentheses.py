class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # when can we add a parenthesis?
        # only add a ')' if # of '(' is > # of ')'
        # only add '(' or ')' if # open parenthesis < n 
        working_stack = []
        result = []
        
        def genParens(num_opens: int, num_closed: int):
            if num_opens == num_closed == n:
                # we found a valid state!
                result.append(''.join(working_stack))
                return
            
            if num_opens < n:
                working_stack.append('(')
                genParens(num_opens + 1, num_closed)
                working_stack.pop()
            
            if num_closed < num_opens:
                working_stack.append(')')
                genParens(num_opens, num_closed + 1)
                working_stack.pop()
                
        genParens(0, 0)
        return result