from typing import List
from collections import Counter

class Solution:
    from collections import Counter
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        couner1 = Counter(nums1)
        counter2 = Counter(nums2)

        intersect = []

        for num in couner1:
            if num in counter2:
                intersect.extend([num] * min(couner1[num], counter2[num]))

        return intersect