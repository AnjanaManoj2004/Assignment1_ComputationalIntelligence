# Assignment1_ComputationalIntelligence
# Assignment1_ComputationalIntelligence
## Task 2: A* Pathfinding for Wheelchair-Accessible Navigation
This project implements the A* pathfinding algorithm to find the optimal path between two locations based on an adjacency matrix and heuristic distances. The environment is represented as a set of locations with their respective distances.
Files required: Task2.py
Requirements
To execute the code, you need Python 3.x installed on your machine.

How to Execute the Code
Clone or Download the Repository:

If you're using Git, clone this repository:
git clone https://github.com/AnjanaManoj2004/Assignment1_ComputationalIntelligence.git
Alternatively, download the repository as a ZIP file and extract it and run the codes.

Navigate to the Project Directory: Use the command line to navigate to the directory where the Python script is located:
cd "C:\Users\ANJANA MANOJ\Desktop\CompIntel"
Run the Python Script: Execute the Python script using Python 3.x:
python3 Task2.py
Choose Start and Goal Locations: When prompted, enter the start and goal location IDs (between 0 and 3). The possible locations are:

0: Golden Leaf Restaurant
1: Residential Area
2: Strip Mall
3: Parking Lot

Example input:
Enter start location (0-3): 0
Enter goal location (0-3): 3
View the Results: The script will display the optimal path from the start location to the goal location, as well as the total cost of the path.

How the Code Works
A Algorithm*: The A* algorithm is implemented using a priority queue (min-heap) to explore the path with the lowest cost. It combines the actual cost to reach the current node (g_score) and the estimated cost to reach the goal (heuristics) to prioritize the nodes.
Manhattan Distance: The heuristic used in this implementation is the Manhattan distance, which is calculated as the sum of the absolute differences in the x and y coordinates between two locations.
Adjacency Matrix: The adjacency matrix represents the travel cost between each pair of locations. If the cost is float('inf'), it indicates that the locations are not directly connected.

Notes
The locations are pre-defined with their geographical coordinates and names.
The adjacency matrix represents the costs between the locations. If no direct path exists, the cost is marked as float('inf').

Troubleshooting
If you receive a "No path found" message, ensure that the start and goal locations are connected and reachable via other locations.
Ensure that the input values for start and goal are integers between 0 and 3.

## Task 3:  A* Pathfinding for Wheelchair-Accessible Navigation considering terrain factors
Description
This project implements the A* pathfinding algorithm to find the optimal path between two locations based on an adjacency matrix and heuristic distances. It also incorporates terrain penalties (uphill and downhill) to calculate the cost of each path. The locations are represented as geographical coordinates, and the terrain constraints are factored into the heuristic calculation using the Manhattan distance.

Files
Task3.py: Contains the implementation of the A* algorithm, adjacency matrix, terrain costs, and the heuristic function.
Requirements
Python 3.x or higher
heapq (standard Python library)

How to Run the Code
Clone or download the repository:
git clone https://github.com/AnjanaManoj2004/Assignment1_ComputationalIntelligence.git
Or download the repository as a ZIP file and extract it.

Navigate to the project directory and execute the python script:

python Task2.py
Choose start and goal locations: When prompted, enter the start and goal location IDs (between 0 and 6).
View the results: The script will display the optimal path from the start location to the goal location, including the total cost of the path considering the terrain penalties.

Code Explanation
A Algorithm*: The A* algorithm is used to find the optimal path by considering both the actual cost (g_score) to reach a node and the heuristic estimate (h_score) to reach the goal. The heuristic used is the Manhattan distance, and terrain penalties are added to the cost when moving between locations.
Manhattan Distance: The Manhattan distance is calculated as the sum of the absolute differences in the x and y coordinates between the start and goal locations.
Terrain Penalties: The terrain cost incorporates penalties for uphill and downhill terrain between locations, making the pathfinding more realistic for wheelchair accessibility.
Adjacency Matrix: The adjacency matrix represents the travel cost between locations. If two locations are not directly connected, the cost is set to infinity (float('inf')).
Heuristic Function
The heuristic used in this implementation is accessibility-aware, incorporating both the Manhattan distance and terrain penalties between locations.
Troubleshooting
If you receive a "No path found" message, ensure that the start and goal locations are connected and reachable via other locations.
Ensure that the input values for start and goal are integers between 0 and 6.

## Task 4: Dijkstra's Algorithm for Finding the Shortest Path with Terrain Constraints
Description
This project implements Dijkstra's algorithm to find the shortest path between two locations in a graph. The locations are represented using an adjacency matrix, and terrain adjustments (e.g., slope and obstacles) are incorporated to modify the cost of traveling between adjacent locations. The terrain-based adjustments are represented as additional penalties that are added to the base cost when traversing between nodes.

Files
Task4.py: Contains the implementation of Dijkstra's algorithm, terrain cost adjustments, and the logic for reconstructing the shortest path from the start to the goal.

Requirements
Python 3.x or higher

How to Run the Code
Clone or download the repository, navigate to the project directory:

Execute the Python script:

python Task4.py
Choose start and goal locations: When prompted, enter the start and goal location IDs (between 0 and 6).
View the results: The script will display the optimal path from the start location to the goal location, including the total cost of the path, considering terrain adjustments.

Code Explanation
Dijkstra's Algorithm: The algorithm finds the shortest path between the start and goal nodes by evaluating paths and considering the minimal cost at each step. The priority queue (min-heap) is used to explore the node with the lowest known distance.
Terrain Adjustments: The terrain costs are applied as penalties when moving between nodes. These terrain-based adjustments may include slopes or other obstacles, which add to the overall cost of the path.
Adjacency Matrix: The adjacency matrix represents the direct travel cost between locations. If a cost is marked as infinity (float('inf')), it means no direct path exists between those locations.
Reconstructing the Path: After finding the shortest path, the code reconstructs the optimal path by tracing back through the parent nodes, starting from the goal node.
Troubleshooting
If you receive a "No path found" message, ensure that the start and goal locations are connected and reachable via other locations.
Ensure that the input values for start and goal are integers between 0 and 6.

## Task 5: GUI Code
Description
The Wheelchair-Friendly Pathfinder is a GUI-based application designed to find the optimal path between two locations, considering terrain penalties (such as slopes and obstacles). The application utilizes Dijkstra's algorithm for shortest path computation and includes a visualization of the path on a canvas, highlighting the best route with terrain-adjusted costs.
The system is especially useful for wheelchair-accessible route planning, helping individuals navigate paths with varying difficulty levels due to terrain.
Features
Dijkstra's Algorithm: Computes the shortest path between a start and goal location while factoring in terrain costs like slopes and obstacles.
Graph Visualization: Displays the map with nodes (locations) and edges (paths) connecting them.
Interactive GUI: Users can select the start and goal locations from dropdown menus and visualize the optimal path on the map.
Terrain Cost Penalties: Includes terrain adjustments based on slopes or obstacles for realistic pathfinding.

Requirements
Python 3.x
Tkinter (comes pre-installed with Python)
heapq (Standard Python Library)

Installation
Clone or download the repository. Ensure you have Python 3.x installed on your system. No external libraries are required beyond Tkinter and heapq, which are included with Python by default.

Run the script:
python Task5.py

Usage
Start Location: Select the starting point from the dropdown menu.
Goal Location: Select the destination from the dropdown menu.
Find Path: Click the "Find Optimal Path" button to compute and display the shortest path with terrain penalties.
Visualization: The optimal path will be highlighted in red on the map, and the path details (locations and cost) will be displayed below the map.
Graph Representation
The graph is represented as an adjacency matrix where the nodes are various locations (e.g., "Golden Leaf", "Residential Area", etc.), and the edges between nodes are weighted with the travel costs. The adjacency matrix is adjusted based on terrain features, which influence the cost (e.g., uphill or downhill penalties).

Code Overview
Key Components:
dijkstra function: Implements Dijkstra’s algorithm to find the shortest path between two locations, adjusting for terrain costs.
reconstruct_path function: Reconstructs the path from the start node to the goal node by backtracking through parent nodes.
GUI: Built with Tkinter to allow the user to interact with the system, select start and goal locations, and display the result visually.
GUI Elements:
Canvas: Displays the locations and paths on a map.
Dropdown Menus: Let users select the start and goal locations.
Result Label: Shows the calculated optimal path and the total cost.
Button: Triggers the pathfinding operation.
