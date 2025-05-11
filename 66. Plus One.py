from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ''
        result = []
        for i in digits:
            s += str(i)
        
        s = int(s)
        s += 1
        
        s = str(s)
        
        for i in s:
            result.append(int(i))
        
        return result