from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i,token in enumerate(tokens):
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "-":
                second_num = stack.pop()
                first_num = stack.pop()
                stack.append(first_num - second_num)
            elif token == "*":
                stack.append(stack.pop()*stack.pop())
            elif token == "/":
                second_num = stack.pop()
                first_num = stack.pop()
                stack.append(int(first_num/second_num))
            else: 
                stack.append(int(token))
        return stack.pop()