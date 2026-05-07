"""Number of islands"""
class Solution:
    """class Solution"""
    def num_islands(self, grid: list[list[str]]) -> int:
        """Function num islands"""

        if not grid:
            return 0

        def dfs(i, j):
            """Function dfs"""

            if (i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == "0"):
                return

            grid[i][j] = "0"

            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        count = 0

        for i, row in enumerate(grid):
            for j, value in enumerate(row):
                if value == "1":
                    dfs(i, j)
                    count += 1

        return count
