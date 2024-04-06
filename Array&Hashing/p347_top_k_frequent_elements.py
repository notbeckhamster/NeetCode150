from typing import List 
import collections

def topKFrequent( nums: List[int], k: int) -> List[int]: # type: ignore
    count_dict = collections.defaultdict(int)
    for each_num in nums:
        count_dict[each_num] += 1
    order_by_count = sorted(count_dict.items(), key = lambda x:x[1], reverse=True)
    top_k_list = []
    for idx in range(k):
        top_k_list.append(order_by_count[idx][0])
    return top_k_list

topKFrequent([1,1,1,2,2,3,2,4,4,4,4,4],2)

