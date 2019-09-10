from typing import List
class Solution(object):
    def maxAreaOfIsland(self, grid: List[List[int]]):
        """ 
            Grid here is 2d array (matrix)
            ---
            This is a BFS problem. Though actually it looks kind of BFS.
        """
        # We label our seen items out of area column to ensure we don't redo it.
        seen = set() # Labelling the places we've seen.
        # Iterates through all ajacent cells then reports when it's seen it
        # |---|---(Not Seen, Digging Further)|---|
        # |---(Not Seen, Digging Further)|X|---(Seen, Not Digging Further)|
        # |---|---(Seen, Not Digging Further)|---|

        # This is the implementation of the BFS
        def area(r, c):
            # We're checking to see if we have a bad row or column index
            # We're also checking to see if we have already seen the code

            if not (0 <= r < len(grid) and 0 <= c < len(grid[0])
                    and (r, c) not in seen and grid[r][c]):
                return 0
            seen.add((r, c))
            # This is now recursively running through each of the nearby nodes on the grid
            # Since we have already searched this node, we get the ones next to it.
            # 1 row down = r + 1
            # 1 row up = r - 1
            # 1 column left = c + 1
            # 1 column right = c - 1
            # This also sets the index +1 if the current location isn't 0. Good for default.
            return (1 + area(r+1, c) + area(r-1, c) +
                    area(r, c-1) + area(r, c+1))
        # This finds the maximum area
        # This is also where we traverse the grid
        # r - stands for row
        # c - stands for column
        # Assuming we skip all seen locations, we should have a finished gred at each position in the array.
        return max(area(r, c)
                   for r in range(len(grid))
                   for c in range(len(grid[0])))

