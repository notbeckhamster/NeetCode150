from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for fixedPtr in range(0,len(nums)-2):
            if fixedPtr > 0 and nums[fixedPtr] == nums[fixedPtr-1]:
                continue
            leftPtr = fixedPtr+1
            rightPtr = len(nums)-1
            fixedVal = -nums[fixedPtr]
            while leftPtr < rightPtr:
                sum = nums[leftPtr] + nums[rightPtr]
                if sum == fixedVal:
                    result.append([nums[fixedPtr],nums[leftPtr], nums[rightPtr]])
                    leftPtr+=1
                    rightPtr-=1
                    while nums[leftPtr] == nums[leftPtr - 1] and leftPtr < rightPtr:
                        l += 1
                elif sum < fixedVal:
                    leftPtr+=1
                else: 
                    rightPtr-=1
        return result