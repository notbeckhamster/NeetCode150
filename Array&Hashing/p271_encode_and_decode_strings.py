from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for each_str in  strs:
            encoded_str += str(len(each_str)) + "#" + each_str
        return encoded_str
    def decode(self, s: str) -> List[str]:
        i=0
        result = []
        while i < len(s):
            j = i
            while(s[j] != "#"):
                j+=1
            length = int(s[i:j])
            result.append(s[j+1:j+1+length])
            i = j+1+length
        return result



solution = Solution()
print(solution.encode(["neet","code","love","you"]))
print(solution.decode(solution.encode(["neet","code","love","you"])))