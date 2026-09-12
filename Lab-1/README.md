# IC-2K23-50-Keshav-Sharma-
# Artificial Intelligence Lab - Lab 1

**Student Details:**
- **Roll No:** IC-2K23-50
- **Name:** Keshav Sharma

---

## Overview

This repository contains implementations of fundamental Artificial Intelligence problem formulations, state space representations, and search algorithms (BFS) for classic AI benchmark problems.

---

## Table of Contents

1. [State Space Representation (8-Puzzle Problem)](#1-state-space-representation-8-puzzle-problem)
2. [Vacuum Cleaner Problem](#2-vacuum-cleaner-problem)
3. [Water Jug Problem](#3-water-jug-problem)
4. [Missionaries and Cannibals Problem](#4-missionaries-and-cannibals-problem)
5. [Prerequisites & Execution](#prerequisites--execution)

---

## 1. State Space Representation (8-Puzzle Problem)

- **File:** `State_Space_Representation.py`
- **Description:** Demonstrates the state space representation and transition model (successor function) for the classic 8-puzzle game.
- **State Representation:** A 9-tuple representing the $3 \times 3$ grid, where `0` denotes the blank/empty tile.
- **Actions:** Moving the blank tile `Up`, `Down`, `Left`, or `Right` within board boundaries.
- **Functionality:** Given an initial state and a goal state, it calculates and displays all valid next states reachable in one step.

### Running the Script:
```bash
python3 State_Space_Representation.py
```

---

## 2. Vacuum Cleaner Problem

- **File:** `Vacuum_cleaner_problem.py`
- **Description:** Implements an intelligent agent for a 2-room environment (`Room A` and `Room B`) that perceives cleanliness status and cleans both rooms systematically.
- **State Representation:**
  - Status of Room A: `Clean` / `Dirty`
  - Status of Room B: `Clean` / `Dirty`
  - Vacuum Location: `A` / `B`
- **Actions:**
  - `Suck dirt` (if current room is dirty)
  - `Move from A to B` / `Move from B to A`
- **Goal:** Both rooms clean (`Room A: Clean`, `Room B: Clean`).

### Running the Script:
```bash
python3 Vacuum_cleaner_problem.py
```

---

## 3. Water Jug Problem

- **File:** `Water_jug.py`
- **Description:** Solves the classic water jug problem using Breadth-First Search (BFS) to find the optimal sequence of steps to measure an exact amount of water.
- **Configuration:**
  - Jug 1 Capacity: 4 Liters
  - Jug 2 Capacity: 3 Liters
  - Target: 2 Liters
- **State Representation:** `(j1, j2)` representing the current volume of water in Jug 1 and Jug 2.
- **Allowed Operations:**
  1. Fill Jug 1 / Fill Jug 2 completely.
  2. Empty Jug 1 / Empty Jug 2.
  3. Pour water from Jug 1 into Jug 2 until full or emptied.
  4. Pour water from Jug 2 into Jug 1 until full or emptied.

### Running the Script:
```bash
python3 Water_jug.py
```

---

## 4. Missionaries and Cannibals Problem

- **File:** `Missionaries_and_Cannibals_Problem.py`
- **Description:** Solves the river crossing puzzle where 3 missionaries and 3 cannibals must cross a river using a boat that can hold at most 2 people, ensuring cannibals never outnumber missionaries on either bank.
- **State Representation:** `(m_left, c_left, boat)`:
  - `m_left`: Number of missionaries on the left bank ($0 \le m \le 3$).
  - `c_left`: Number of cannibals on the left bank ($0 \le c \le 3$).
  - `boat`: `0` if on the left bank, `1` if on the right bank.
- **Search Strategy:** Breadth-First Search (BFS) with state validation and cycle prevention (visited set) to produce the step-by-step path from `(3, 3, 0)` to `(0, 0, 1)`.

### Running the Script:
```bash
python3 Missionaries_and_Cannibals_Problem.py
```

---

## Prerequisites & Execution

- **Environment:** Python 3.x
- **Standard Libraries Used:** `collections` (`deque`)
- Run all scripts directly using the standard Python 3 interpreter.
