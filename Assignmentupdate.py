# ID : 011182073
# Iftekhar Mahmud
def heuristic(node, goal):
    x, y = node
    if (x, y) == goal:
        return 0
    return 1 / ((x - goal[0]) ** 2 + (y - goal[1]) ** 2)

def astar(grid, start, goal):
    max_x = len(grid[0]) - 1
    max_y = len(grid) - 1

    open_list = [(0, start, [])]
    closed_set = set()

    while open_list:
        cost, node, path = min(open_list, key=lambda x: x[0])
        open_list.remove((cost, node, path))

        if node in closed_set:
            continue

        x, y = node
        if node == goal:
            return path + [node]

        closed_set.add(node)
        for i, j in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_x, new_y = x + i, y + j
            if 0 <= new_x < len(grid[0]) and 0 <= new_y < len(grid) and grid[new_y][new_x] != 'O':
                new_cost = cost + heuristic((new_x, new_y))
                open_list.append((new_cost + heuristic((new_x, new_y), goal), (new_x, new_y), path + [(x, y)]))

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
goal = (2, 4)


path = astar(grid, start, goal)


print(f"Output: {goal} is the cell with Carbon Monoxide")
print("Path:")
for node in path:
    print(node)
