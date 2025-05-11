from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = []
        for i in range(len(nums)):
            if nums[i] == target:
                result.append(i)
                break

        for j in range(len(nums) - 1, 0, -1):
            if nums[j] == target:
                result.append(j)
                break
            
        if len(result) == 0:
            result.append(-1)
            result.append(-1)
            return result

        elif len(result) == 1:
            result.append(result[0])
            return result

        else:
            return result