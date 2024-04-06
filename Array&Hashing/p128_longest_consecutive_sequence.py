from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        largestSequence = 0 
        
        for num in nums:
            #check num is start 
            if num-1 not in nums_set:
                seqSize = 0
                curr_num = num
                while curr_num in nums_set:
                    seqSize+=1
                    curr_num+=1
                if seqSize > largestSequence:
                    largestSequence = seqSize
        return largestSequence

