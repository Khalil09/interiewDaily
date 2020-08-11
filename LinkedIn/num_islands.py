class Solution(object):
    def inRange(self, grid, r, c):
        numRow, numCol = len(grid), len(grid[0])
        if r < 0 or c < 0 or r >= numRow or c >= numCol:
            return False
        return True

    def numIslands(self, grid):

        def dfs(grid, l, c):
            directions = [(1, 0), (0, 1), (-1 ,0), (0, -1)]
            for dir in directions:
                new_line, new_column = dir[0] + l, dir[1] + c
                if self.inRange(grid, new_line, new_column) and \
                   grid[new_line][new_column] == 1:
                        grid[new_line][new_column] = 2
                        dfs(grid, new_line, new_column)

        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    grid[i][j] = 2
                    dfs(grid, i, j)
                    islands += 1

        return islands

# Each number 1 is node in a graph. Adjcents 1 represent a undirection connection 

grid = [[1, 1, 0, 1, 0],
        [0, 1, 0, 0, 1],
        [1, 0, 0, 1, 1],
        [0, 1, 0, 1, 1]]

print(Solution().numIslands(grid))
# 3
