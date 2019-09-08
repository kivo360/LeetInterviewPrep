from collections import Counter
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Counter is a godsend for these kinds of problems.
        # It gets the number of occurences of each item in the list in the most efficient manner
        number_counts = Counter(nums)
        # Now that we have the number of occurences we're iterating through them here.
        for k, v in number_counts.items():
            # We return the index for the number that has only a single occurence.
            if v == 1: 
                return k # this is the value of the single occurence.
        return 0