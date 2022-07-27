class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # define rows and columns
        r, c = len(grid), len(grid[0])
        
        def dfs(i,j):
            if i < 0 or j<0 or i>=r or j >= c or grid[i][j] ==0:
                return 0
            grid[i][j] =0
            top = dfs(i-1, j)
            bot = dfs(i+1,j)
            left = dfs(i, j-1)
            right = dfs(i, j+1)
            return 1 + top + bot + left + right
        count = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] ==1:
                    temp = dfs(i,j)
                    count = max(temp, count)
        return count