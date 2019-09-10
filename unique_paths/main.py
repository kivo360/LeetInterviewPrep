class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        if m == 0 and n == 0:
            return 0
        # This creates a matrix to iterate on, where n is the column and m is the row
        aux = [[1 for x in range(n)] for x in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                # We start with 1 to allow for reductions throughout the code base
                # Index I, and J has an added index comparatively???? What the fuck?
                # aux[1, 1] = 1 + 1 = 2
                # aux[2, 1] = 2+1 = 3 
                # This basically adds the grid information together
                aux[i][j] = aux[i][j-1]+aux[i-1][j]
        return aux[-1][-1]