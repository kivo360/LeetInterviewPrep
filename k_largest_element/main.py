import heapq
from typing import List
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        heapq.heapify(heap)
        
        for row in nums:
            heapq.heappush(heap, row)
        
        largest = heapq.nlargest(k, heap)
        return largest[-1]