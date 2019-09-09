from typing import  List
import queue, collections


BASKETS = 2


class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        largest = 0  # The largest in history.
        ntotal = 0  # The current amount of total fruits.
        nlast = 0  # The current amount of the last repeated fruits.
        
        dq = collections.deque(maxlen=BASKETS)
        
        for fruit in tree:
            if fruit in dq:
                ntotal += 1
                if fruit != dq[-1]:
                    nlast = 1
                    dq.remove(fruit)
                    dq.append(fruit)
                else:
                    nlast += 1
            else:
                ntotal = nlast + 1
                nlast = 1
                dq.append(fruit)  # dq will popleft if it's full.
            
            if ntotal > largest:
                largest = ntotal
        return largest