import heapq

class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0  # cost from start node to current node
        self.h = 0  # heuristic estimate from current node to goal node
        self.f = 0  # total cost: f = g + h

    def __lt__(self, other):
        return self.f < other.f

def astar(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    open_set = []   # priority queue for nodes to be evaluated
    closed_set = set()  # set of nodes already evaluated

    start_node = Node(start)
    goal_node = Node(goal)

    heapq.heappush(open_set, start_node)

    while open_set:
        current_node = heapq.heappop(open_set)

        if current_node.position == goal_node.position:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]  # reverse the path to get from start to goal

        closed_set.add(current_node.position)

        for neighbor_position in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            neighbor_row, neighbor_col = current_node.position[0] + neighbor_position[0], current_node.position[1] + neighbor_position[1]

            if 0 <= neighbor_row < rows and 0 <= neighbor_col < cols and grid[neighbor_row][neighbor_col] == 0:
                neighbor = Node((neighbor_row, neighbor_col), current_node)

                if neighbor.position in closed_set:
                    continue

                neighbor.g = current_node.g + 1
                neighbor.h = abs(neighbor.position[0] - goal_node.position[0]) + abs(neighbor.position[1] - goal_node.position[1])
                neighbor.f = neighbor.g + neighbor.h

                if neighbor not in open_set:
                    heapq.heappush(open_set, neighbor)

    return None  # No path found

# Example usage:
grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0]
]
start = (0, 0)
goal = (4, 4)
result = astar(grid, start, goal)

if result:
    print("Path found:", result)
else:
    print("No path found.")
