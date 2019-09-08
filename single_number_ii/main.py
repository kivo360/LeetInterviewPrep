from collections import Counter
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        number_counts = Counter(nums)
        for k, v in number_counts.items():
            if v == 1:
                return k
        return 0