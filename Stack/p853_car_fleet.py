from typing import List
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(position, speed) for position, speed in zip(position, speed)]
        pairs.sort(reverse=True)
        stack = []
        for pos, s in pairs: # type: ignore
            stack.append((target-pos)/s)
            if len(stack)>=2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)