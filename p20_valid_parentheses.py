class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_to_open_map = {"}":"{", ")":"(", "]":"["}
        for char in s: 
            if char in "({[":
                stack.append(char)
            else:
                if len(stack) > 0:
                    last_bracket = stack.pop()
                    if close_to_open_map[char] != last_bracket:
                        return False
                else:
                    return False
        return len(stack) == 0