class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        record = set()
        def traverse(h:int, idx:int) -> None:
            if f"{h}:{idx}" in record:
                return
            record.add(f"{h}:{idx}")
            if h+1 < len(grid) and grid[h+1][idx] == '1':
                traverse(h+1, idx)
            if h-1 >= 0 and grid[h-1][idx] == '1':
                traverse(h-1, idx)
            if idx+1 < len(grid[h]) and grid[h][idx+1] == '1':
                traverse(h, idx+1)
            if idx-1 >= 0 and grid[h][idx-1] == '1':
                traverse(h, idx-1)
            return 
        counter = 0
        for h in range(len(grid)):
            for idx in range(len(grid[h])):
                if grid[h][idx] == '1' and f"{h}:{idx}" not in record:
                    traverse(h, idx)
                    counter += 1
        # print(counter)
        print(record)
        return counter

        