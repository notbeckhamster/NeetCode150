from typing import List 

def productExceptSelf( nums: List[int]) -> List[int]: # type: ignore
    left_to_right_arr = [nums[0]]*len(nums)
    right_to_left_arr = [nums[len(nums)-1]]*len(nums)

    for idx in range(1,len(nums), 1):
        left_to_right_arr[idx] = left_to_right_arr[idx-1]*nums[idx]
    for idx in range(len(nums)-2, -1, -1):
        right_to_left_arr[idx] = right_to_left_arr[idx+1]*nums[idx]
    
    output = [0]*len(nums)
    for idx in range(len(nums)):
        left_val = left_to_right_arr[idx-1] if idx>0 else 1
        right_val = right_to_left_arr[idx+1] if idx<len(nums)-1 else 1
        output[idx] = left_val*right_val
    return output

print(productExceptSelf([1,2,3,4]))