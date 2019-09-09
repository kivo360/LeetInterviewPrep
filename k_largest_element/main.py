import heapq
from typing import List
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """ 
            Expected Input:
                - list of ints
                - the position in a sorted array that we want to discover
        
            Believed Solution:
                - That because this is a sorting problem we should use a heap to solve the problem
                - Python has built-in heap solutions that contribute to the answer, mainly heapq
        """

        heap = []
        heapq.heapify(heap)
        
        for row in nums:
            heapq.heappush(heap, row)
        
        largest = heapq.nlargest(k, heap)
        return largest[-1]