class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        cols = []
        result = 0
        for i in range(n):
            col = []
            for row in grid:
                col.append(row[i])
            cols.append(col)
        
        for i in range(n):
            for j in range(n):
                if grid[i] == cols[j]:
                    result += 1
        
        return result

        