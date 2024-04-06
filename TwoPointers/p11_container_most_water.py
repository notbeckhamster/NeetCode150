from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        max_area = 0
        while l<r:
            lower_h = min(height[l], height[r])
            x_len = r - l 
            area = lower_h * x_len
            if area > max_area:
                max_area = area
            if height[l] < height[r]:
                l+=1
            else:
                r-=1
        return max_area
