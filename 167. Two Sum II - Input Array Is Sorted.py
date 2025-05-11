from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left, right = 0, len(numbers) - 1
        while left < right:
            summa = numbers[left] + numbers[right]
            if summa > target:
                right -= 1
            elif summa < target:
                left += 1
            else:
                return [left + 1, right + 1]