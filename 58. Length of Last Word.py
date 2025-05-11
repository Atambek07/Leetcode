class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        k = s.split()
        result = len(k[-1])

        return result