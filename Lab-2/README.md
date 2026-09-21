# IC-2K23-50-Keshav-Sharma-
# Artificial Intelligence Lab - Lab 2

**Student Details:**
- **Roll No:** IC-2K23-50
- **Name:** Keshav Sharma

---

## Overview

This repository contains implementations of fundamental graph traversal, search, and problem-solving algorithms in Artificial Intelligence, focusing on **Breadth-First Search (BFS)**, **Depth-First Search (DFS)**, and **Informed A* Search**. These techniques are applied to:
1. Abstract graph traversals.
2. Maze solving with backtracking.
3. Robot path planning in obstacle grids.
4. Inter-city route planning across connected networks.
5. The classic 8-puzzle sliding tile game using Manhattan distance heuristics.

---

## Table of Contents

1. [Graph Traversal using BFS and DFS](#1-graph-traversal-using-bfs-and-dfs)
2. [Maze Solver using DFS](#2-maze-solver-using-dfs)
3. [Robot Navigation using BFS](#3-robot-navigation-using-bfs)
4. [Route Planning using BFS](#4-route-planning-using-bfs)
5. [8-Puzzle Solver using A* Search](#5-8-puzzle-solver-using-a-search)
6. [Comparison: BFS vs. DFS vs. A* Search](#comparison-bfs-vs-dfs-vs-a-search)
7. [Prerequisites & Execution](#prerequisites--execution)

---

## 1. Graph Traversal using BFS and DFS

- **File:** `Graph_Traversal_using_BFS_and_DFS.py`
- **Description:** Implements and compares standard Breadth-First Search (BFS) and Depth-First Search (DFS) traversals on an unweighted directed graph.
- **Graph Representation:** Adjacency list using a Python dictionary:
  ```python
  graph = {
      'A': ['B', 'C'],
      'B': ['D', 'E'],
      'C': ['F'],
      'D': [],
      'E': ['F'],
      'F': []
  }
  ```
- **Algorithms Implemented:**
  - **BFS (Breadth-First Search):** Explores neighbor nodes level-by-level using a FIFO queue (`collections.deque`) and a visited set to avoid cycles.
  - **DFS (Depth-First Search):** Explores along each branch as deep as possible before backtracking using recursive calls and a visited set.

### Running the Script:
```bash
python3 Graph_Traversal_using_BFS_and_DFS.py
```

---

## 2. Maze Solver using DFS

- **File:** `Maze_Solver_using_DFS.py`
- **Description:** Solves a 2D grid-based maze puzzle from a start position to a goal destination using recursive Depth-First Search with backtracking.
- **Grid Representation:**
  - `'S'`: Start Position
  - `'G'`: Goal Position
  - `'0'`: Walkable open cell
  - `'1'`: Impassable wall / obstacle
  - `'*'`: Marked path solution
- **Movement Rules:** 4-directional transitions (`Up`, `Down`, `Left`, `Right`).
- **Algorithm Strategy:**
  - Validates grid boundaries and obstacle collisions.
  - Recursively searches neighboring cells.
  - Backtracks (`path.pop()`) when reaching dead-ends until a valid route to `'G'` is discovered.

### Running the Script:
```bash
python3 Maze_Solver_using_DFS.py
```

---

## 3. Robot Navigation using BFS

- **File:** `Robot_Navigation_using_BFS.py`
- **Description:** Implements an autonomous robot navigation agent navigating a 2D grid containing obstacles to find the shortest path from the starting position to the goal destination.
- **Grid Representation:**
  - `'R'`: Initial Robot position
  - `'G'`: Target Goal position
  - `'0'`: Free navigable space
  - `'1'`: Obstacle / barrier
  - `'*'`: Optimal traversed route
- **Algorithm Strategy:**
  - Utilizes Breadth-First Search (BFS) with a queue (`collections.deque`) storing `(current_cell, path_so_far)`.
  - Guarantees finding the shortest path (minimum number of steps) in an unweighted grid.
  - Marks the final path on the grid for visual verification.

### Running the Script:
```bash
python3 Robot_Navigation_using_BFS.py
```

---

## 4. Route Planning using BFS

- **File:** `Route_Planning_using_BFS.py`
- **Description:** Implements route planning between cities (e.g., from Indore to Jabalpur) across a connected network map using Breadth-First Search (BFS).
- **Graph Representation:** Adjacency list mapping cities to adjacent destinations:
  ```python
  graph = {
      "Indore": ["Bhopal", "Ujjain"],
      "Bhopal": ["Indore", "Jabalpur", "Sagar"],
      "Ujjain": ["Indore", "Ratlam"],
      "Jabalpur": ["Bhopal", "Katni"],
      "Sagar": ["Bhopal"],
      "Ratlam": ["Ujjain", "Neemuch"],
      "Katni": ["Jabalpur"],
      "Neemuch": ["Ratlam"]
  }
  ```
- **Algorithm Strategy:**
  - Uses a FIFO queue (`collections.deque`) initialized with `[[start]]` paths.
  - Explores routes layer by layer to guarantee the shortest route (fewest transit stops/hops) between source and destination.
  - Maintains a `visited` set to prevent revisiting cities and infinite loops.

### Running the Script:
```bash
python3 Route_Planning_using_BFS.py
```

---

## 5. 8-Puzzle Solver using A* Search

- **File:** `8-Puzzle_Solver.py`
- **Description:** Solves the classic 3x3 8-puzzle sliding tile problem from an initial disordered state to the canonical goal configuration using the **A* Search algorithm** guided by the **Manhattan Distance heuristic**.
- **State Representation:** 1D tuple of 9 numbers where `0` denotes the empty space:
  - **Goal State:** `(1, 2, 3, 4, 5, 6, 7, 8, 0)`
- **Evaluation Function:**
  $$f(n) = g(n) + h(n)$$
  - $g(n)$: Exact path cost from start state to node $n$ (number of moves made).
  - $h(n)$: Heuristic estimate calculated as the sum of Manhattan distances of all tiles from their goal positions:
    $$\text{Manhattan Distance} = |r_{\text{current}} - r_{\text{goal}}| + |c_{\text{current}} - c_{\text{goal}}|$$
- **Algorithm Strategy:**
  - Employs a Min-Priority Queue (`heapq`) storing elements ordered by lowest $f(n)$ value.
  - Dynamically computes valid slide operations (`Up`, `Down`, `Left`, `Right`) based on the position of `0`.
  - Avoids revisited states using a closed set (`visited`).
  - Outputs the step count and visual 3x3 board matrices for every step along the optimal path.

### Running the Script:
```bash
python3 8-Puzzle_Solver.py
```

---

## Comparison: BFS vs. DFS vs. A* Search

| Feature | Breadth-First Search (BFS) | Depth-First Search (DFS) | A* Search |
| :--- | :--- | :--- | :--- |
| **Search Type** | Uninformed / Blind | Uninformed / Blind | Informed / Heuristic |
| **Data Structure** | Queue (FIFO) | Stack (LIFO) / Recursion | Priority Queue (Min-Heap) |
| **Search Strategy** | Level-by-level exploration | Deep branch exploration with backtracking | Best-first expansion via $f(n) = g(n) + h(n)$ |
| **Optimality** | Guarantees shortest path (unweighted) | Does not guarantee shortest path | Guaranteed optimal with admissible heuristic |
| **Completeness** | Complete (finite branching) | Complete (finite state spaces) | Complete |
| **Lab Applications** | Robot Navigation, Route Planning | Maze Solving, Graph Traversal | 8-Puzzle Solver |

---

## Prerequisites & Execution

- **Environment:** Python 3.x
- **Standard Libraries Used:** `collections` (`deque`), `heapq`
- To run any of the lab experiments, navigate to the `Lab-2` directory and execute:
  ```bash
  cd Lab-2
  python3 Graph_Traversal_using_BFS_and_DFS.py
  python3 Maze_Solver_using_DFS.py
  python3 Robot_Navigation_using_BFS.py
  python3 Route_Planning_using_BFS.py
  python3 8-Puzzle_Solver.py
  ```

