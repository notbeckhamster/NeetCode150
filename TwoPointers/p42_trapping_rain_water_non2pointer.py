class Solution:
    def trap(self, height: list[int]) -> int:
        max_left = [0]*len(height)
        for i in range(1, len(max_left)):
            max_left[i] = max(max_left[i-1], height[i-1])
        max_right = [0]*len(height)
        for i in range(len(max_right)-2, -1, -1):
            max_right[i] = max(max_right[i+1], height[i+1])
        min_height = [min(max_left[i], max_right[i]) for i in range(len(height))]
        sum_water = 0
        for idx, h in enumerate(height):
            water_in_h = min_height[idx] -h
            if water_in_h > 0:
                sum_water += water_in_h
        return sum_water

        