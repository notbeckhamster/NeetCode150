from typing import List
import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        chars_to_list_map = collections.defaultdict(list)
        for each_string in strs:
            char_count_arr = [0]*26
            for each_char in each_string:
                char_count_arr[ord(each_char) - ord('a')] += 1
            chars_to_list_map[tuple(char_count_arr)].append(each_string)
        return chars_to_list_map.values()  # type: ignore