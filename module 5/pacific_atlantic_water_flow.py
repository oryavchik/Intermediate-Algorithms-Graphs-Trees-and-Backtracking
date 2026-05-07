"""Pacific atlantic water flow"""

class Solution:
    """class Solution"""
    def pacific_atlantic(self, heights: list[list[int]]) -> list[list[int]]:
        """Function pacific atlantic"""
        if not heights:
            return []

        m = len(heights)
        n = len(heights[0])

        pacific_reachable = []

        for _ in range(m):
            row = []
            for _ in range(n):
                row.append(False)

            pacific_reachable.append(row)

        atlantic_reachable = []

        for _ in range(m):
            row = []

            for _ in range(n):
                row.append(False)

            atlantic_reachable.append(row)

        def dfs(row, col, reachable):
            """Function dfs"""
            reachable[row][col] = True

            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for dr, dc in directions:
                newrow = row + dr
                newcol = col + dc

                if (0 <= newrow < m and 0 <= newcol < n and not reachable[newrow][newcol]
                    and heights[newrow][newcol] >= heights[row][col]):
                    dfs(newrow, newcol, reachable)

        for i in range(m):
            dfs(i, 0, pacific_reachable)
            dfs(i, n - 1, atlantic_reachable)

        for j in range(n):
            dfs(0, j, pacific_reachable)
            dfs(m - 1, j, atlantic_reachable)

        result = []

        for i, row in enumerate(heights):
            for j, _ in enumerate(row):
                if (pacific_reachable[i][j] and atlantic_reachable[i][j]):
                    result.append([i, j])

        return result
