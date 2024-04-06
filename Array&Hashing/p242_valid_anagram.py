class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hashset = set()
        t_hashset = set()
        for idx, s_char in enumerate(s):
            t_char = t[idx]
            s_hashset.add(s_char)
            t_hashset.add(t_char)
        return s_hashset == t_hashset