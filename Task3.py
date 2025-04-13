import heapq

# 0 = Golden Leaf, 1 = Residential Area, 2 = Strip Mall, 3 = Parking Lot, 4 = Burwood Teppanyaki House, 5 = Petrol Pump, 6 = Burwood One Shopping Centre
adj_matrix = [
    [0, 1, float('inf'), float('inf'), 1, float('inf'), float('inf')],  # Golden Leaf
    [1, 0, float('inf'), 8, float('inf'), 10, 7],            # Residential Area
    [float('inf'), float('inf'), 0, 1, float('inf'), float('inf'), float('inf')],  # Strip Mall
    [float('inf'), 8, 1, 0, 3, float('inf'), float('inf')],             # Parking Lot
    [1, float('inf'), float('inf'), 3, 0, float('inf'), float('inf')],  # Teppanyaki
    [float('inf'), 10, float('inf'), float('inf'), float('inf'), 0, float('inf')],  # Petrol Pump
    [float('inf'), 7, float('inf'), float('inf'), float('inf'), float('inf'), 0]   # Burwood One Shopping Centre
]

# Asymmetric terrain penalties: uphill = higher penalty, downhill = lower
terrain_costs = {
    (1, 0): 3,  # Residential Area -> Golden Leaf (uphill)
    (3, 0): 1,  # Parking Lot -> Golden Leaf (downhill)
    (0, 3): 1,  # Golden Leaf -> Parking Lot (downhill)
    (1, 6): 3,  # Residential Area -> Burwood One (uphill)
    (6, 1): 1,  # Burwood One -> Residential Area (downhill)
    (1, 5): 3,  # Residential Area -> Petrol Pump (uphill)
    (5, 1): 1,  # Petrol Pump -> Residential Area (downhill)
    (4, 3): 2,  # Teppanyaki -> Parking Lot (uphill)
    (3, 4): 1,  # Parking Lot -> Teppanyaki (downhill)
    (2, 3): 1,  # Strip Mall -> Parking Lot (uphill)
    (3, 2): 1   # Parking Lot -> Strip Mall (slight uphill/downhill)
}

# Coordinates for Manhattan distance (used in heuristics)
locations = {
    0: (-37.876, 145.112),  # Golden Leaf
    1: (-37.875, 145.116),  # Residential Area
    2: (-37.877, 145.120),  # Strip Mall
    3: (-37.878, 145.119),  # Parking Lot
    4: (-37.876, 145.121),  # Teppanyaki
    5: (-37.879, 145.122),  # Petrol Pump
    6: (-37.880, 145.123)   # Burwood One Shopping Centre
}

# Manhattan Distance
def manhattan_distance(start, end):
    x1, y1 = start
    x2, y2 = end
    return abs(x1 - x2) + abs(y1 - y2)

# Heuristic that incorporates terrain constraints
def accessibility_aware_heuristic(start, goal):
    base_distance = manhattan_distance(locations[start], locations[goal])
    terrain_penalty = terrain_costs.get((start, goal), 0)
    return base_distance + terrain_penalty

# A* algorithm
def a_star(adj_matrix, heuristics, start, goal):
    num_nodes = len(adj_matrix)
    open_list = []
    heapq.heappush(open_list, (heuristics[start][goal], 0, start))  # (f_score, g_score, node)

    g_score = {node: float('inf') for node in range(num_nodes)}
    g_score[start] = 0
    parent_node = {node: None for node in range(num_nodes)}

    while open_list:
        _, current_g, current_node = heapq.heappop(open_list)

        if current_node == goal:
            return reconstruct_path(parent_node, goal)

        for neighbor, cost in enumerate(adj_matrix[current_node]):
            if cost != float('inf'):
                terrain_penalty = terrain_costs.get((current_node, neighbor), 0)
                tentative_g = current_g + cost + terrain_penalty

                if tentative_g < g_score[neighbor]:
                    g_score[neighbor] = tentative_g
                    parent_node[neighbor] = current_node
                    f_score = tentative_g + heuristics[neighbor][goal]
                    heapq.heappush(open_list, (f_score, tentative_g, neighbor))

    return None  # No path found

# Reconstruct path from end to start
def reconstruct_path(parent_node, goal):
    path = []
    while goal is not None:
        path.append(goal)
        goal = parent_node[goal]
    return path[::-1]

# Pre-calculate heuristics with terrain-aware function
heuristics = {}
for start in locations:
    heuristics[start] = {}
    for goal in locations:
        heuristics[start][goal] = accessibility_aware_heuristic(start, goal)

# Friendly names for locations
location_names = {
    0: "Golden Leaf Chinese Restaurant",
    1: "Residential Area",
    2: "Strip Mall",
    3: "Parking Lot",
    4: "Burwood Teppanyaki House",
    5: "Petrol Pump",
    6: "Burwood One Shopping Centre"
}

print("\nChoose your start and goal location:")
for idx, name in location_names.items():
    print(f"{idx}: {name}")
# Input
start = int(input("Enter the start location (0-6): "))  
goal = int(input("Enter the goal location (0-6): "))

# Run A*
path = a_star(adj_matrix, heuristics, start, goal)

# Display result
if path:
    print("\nOptimal path found:")
    for step in path:
        print(f" -> {location_names[step]}", end="")
    total_cost = 0
    for i in range(len(path)-1):
        u, v = path[i], path[i+1]
        base = adj_matrix[u][v]
        penalty = terrain_costs.get((u, v), 0)
        total_cost += base + penalty
    print(f"\n Total cost (with terrain): {total_cost}")
else:
    print("No path found.")
