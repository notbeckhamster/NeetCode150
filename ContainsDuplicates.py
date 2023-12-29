from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        #Iterate entire list check if last element equal
        last_num = -1
        for num in nums:
            if (num == last_num): 
                return True
            last_num = num
        return False
