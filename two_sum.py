
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        old_nums = nums.copy()
        nums.sort()
        #Use 2 pointers
        left_pt = 0
        right_pt = len(nums)-1
        while (left_pt<right_pt):
            result = nums[left_pt] + nums[right_pt]
            if result == target:
                return [old_nums.index(nums[left_pt]), old_nums.index(nums[right_pt])]
            elif result < target:
                left_pt +=1
            else:
                right_pt-=1
        return [-1,-1]