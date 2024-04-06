class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_s = ""
        for char in s:
            if char.isalpha() or char.isdigit():
                filtered_s += char.lower()
        return filtered_s == filtered_s[::-1]