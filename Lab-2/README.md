# IC-2K23-50-Keshav-Sharma-
# Artificial Intelligence Lab - Lab 2

**Student Details:**
- **Roll No:** IC-2K23-50
- **Name:** Keshav Sharma

---

## Overview

This repository contains implementations of fundamental graph traversal and search algorithms in Artificial Intelligence, focusing on **Breadth-First Search (BFS)** and **Depth-First Search (DFS)**. These techniques are applied to abstract graph traversals, maze solving with backtracking, and robot path planning in obstacle grids.

---

## Table of Contents

1. [Graph Traversal using BFS and DFS](#1-graph-traversal-using-bfs-and-dfs)
2. [Maze Solver using DFS](#2-maze-solver-using-dfs)
3. [Robot Navigation using BFS](#3-robot-navigation-using-bfs)
4. [Comparison: BFS vs. DFS](#comparison-bfs-vs-dfs)
5. [Prerequisites & Execution](#prerequisites--execution)

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

## Comparison: BFS vs. DFS

| Feature | Breadth-First Search (BFS) | Depth-First Search (DFS) |
| :--- | :--- | :--- |
| **Data Structure** | Queue (FIFO) | Stack (LIFO) / Recursion |
| **Search Strategy** | Level-by-level exploration | Deep branch exploration with backtracking |
| **Optimality** | Guarantees shortest path in unweighted graphs | Does not guarantee shortest path |
| **Memory Complexity** | Higher ($O(b^d)$) | Lower ($O(b \cdot m)$) |
| **Application in Lab** | Robot Navigation (Shortest Path) | Maze Solving (Path Existence / Backtracking) |

---

## Prerequisites & Execution

- **Environment:** Python 3.x
- **Standard Libraries Used:** `collections` (`deque`)
- To run any of the lab experiments, navigate to the `Lab-2` directory and execute:
  ```bash
  cd Lab-2
  python3 Graph_Traversal_using_BFS_and_DFS.py
  python3 Maze_Solver_using_DFS.py
  python3 Robot_Navigation_using_BFS.py
  ```
