from collections import deque

def solve_water_jug(jug1_cap, jug2_cap, target):
    queue = deque([((0, 0), [])])
    visited = set((0, 0))
    
    while queue:
        (j1, j2), path = queue.popleft()
        
        current_path = path + [(j1, j2)]
        
        if j1 == target or j2 == target:
            return current_path
            
        moves = [
            (jug1_cap, j2), 
            (j1, jug2_cap),     
            (0, j2),            
            (j1, 0),            
            (max(0, j1 - (jug2_cap - j2)), min(jug2_cap, j1 + j2)),
            (min(jug1_cap, j1 + j2), max(0, j2 - (jug1_cap - j1)))
        ]
        
        for move in moves:
            if move not in visited:
                visited.add(move)
                queue.append((move, current_path))
                
    return None 

j1_capacity = 4
j2_capacity = 3
goal = 2

solution = solve_water_jug(j1_capacity, j2_capacity, goal)

if solution:
    print(f"Solution found in {len(solution) - 1} steps:")
    for step, state in enumerate(solution):
        print(f"Step {step}: Jug1 = {state[0]}L, Jug2 = {state[1]}L")
else:
    print("No solution is possible for these capacities and target.")
