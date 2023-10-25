import heapq

def astar(grid, start):
    max_x = len(grid[0]) - 1
    max_y = len(grid) - 1

    open_list = [(0, start, [])]
    heapq.heapify(open_list)
    closed_set = set()

    while open_list:
        cost, node, path = heapq.heappop(open_list)

        if node in closed_set:
            continue

        x, y = node
        if node != start and grid[y][x] == grid[start[1]][start[0]]:
            return path + [(x, y)]

        closed_set.add(node)

        for i, j in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_x, new_y = x + i, y + j
            if 0 <= new_x <= max_x and 0 <= new_y <= max_y and grid[new_y][new_x] != 'O':
                new_cost = cost + 1
                heapq.heappush(open_list, (new_cost, (new_x, new_y), path + [(x, y)]))

    return None

grid = [
    [42, 48, 55, 58, 59, 58],
    [44, 50, 56, 'O', 61, 60],
    [45, 49, 57, 'O', 65, 62],
    [39, 45, 55, 60, 'O', 60],
    [38, 40, 50, 55, 59, 58],
    [37, 45, 48, 49, 50, 49],
]

start = (4, 1)
path = astar(grid, start)

print(f"Path to the highest value: {path}")
