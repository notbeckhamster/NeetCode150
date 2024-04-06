from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        while l<=r:
            m = int(l + (r-l)/2)
            print(m)
            m_val = nums[m]
            if m_val == target:
                return m
            elif m_val > target:
                r = m-1
            else:
                l=m+1
        return -1