class Solution:
    def isPalindrome(self, s: str) -> bool:

        filtered = "".join(filter(str.isalnum, s))
        filtered = filtered.lower()

        return filtered == filtered[::-1]
