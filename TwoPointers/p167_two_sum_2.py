from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]: # type: ignore
        leftPtr = 0
        rightPtr = len(numbers)-1
        while (leftPtr < rightPtr):
            sum = numbers[leftPtr] + numbers[rightPtr]
            if (sum == target):
                return [leftPtr+1, rightPtr+1]
            elif (sum > target):
                rightPtr-=1
            else:
                leftPtr+=1