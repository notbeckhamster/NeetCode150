from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        result = []
        stack.append("")
        self.n = n
        self.dfs(0, 0, stack, result)
        return result
    def dfs(self, num_open, num_closed, stack, result):
        curr = stack.pop()
        if num_open == num_closed == self.n:
            result.append(curr)
        if num_closed < num_open:
            next_parenthese = curr[:] + ")"
            stack.append(next_parenthese)
            self.dfs(num_open, num_closed+1, stack, result)
        if num_open < self.n:
            next_parenthese = curr[:] + "("
            stack.append(next_parenthese)
            self.dfs(num_open+1, num_closed, stack, result)

        