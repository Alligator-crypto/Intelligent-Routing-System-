#!/usr/bin/env python
# coding: utf-8

# In[4]:


import heapq

# Core Network Topography (10 Transit Hubs with true link distances)
network_map = {
    "S":{"A":2, "B":5},
    "A":{"C":4,"D":7},
    "B":{"D":3, "E":6},
    "C":{"F":5},
    "D":{"F":2,"G":3},
    "E":{"G":1},
    "F":{"H":3},
    "G":{"H":2},
    "H":{},
    "I":{}
}

# Heuristic Optimizers (Estimated straight-line distance to Target Hub H)
target_heuristics = {"S":10,"A":8, "B":7, "C":6,"D":4, "E":3, "F":2,"G":1, "H":0, "I":5}

def compute_bfs(graph,start,goal):
    visited = []
    queue = [[start]]
    nodes_processed = 0
    if start == goal:
        return [start],nodes_processed
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node not in visited:
            nodes_processed += 1
            if node == goal:
                return path,nodes_processed
            visited.append(node)
            for neighbor in graph.get(node,{}):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
    return None,nodes_processed

def compute_ucs(graph,start,goal):
    pq = [(0,start,[start])]
    visited = []
    nodes_processed = 0
    while pq:
        cost,node,path = heapq.heappop(pq)
        if node in visited:
            continue
        nodes_processed += 1
        visited.append(node)
        if node == goal:
            return path,cost,nodes_processed
        for neighbor,edge_cost in graph.get(node,{}).items():
            if neighbor not in visited:
                heapq.heappush(pq,(cost + edge_cost,neighbor,path + [neighbor]))
    return None,float("inf"),nodes_processed

def compute_astar(graph,start,goal,heuristics):
    open_list = []
    visited = []
    heapq.heappush(open_list,(heuristics[start],0,start,[start]))
    nodes_processed = 0
    while open_list:
        f,g,current,path = heapq.heappop(open_list)
        if current in visited:
            continue
        nodes_processed += 1
        visited.append(current)
        if current == goal:
            return path,g,nodes_processed
        for neighbor,cost in graph.get(current,{}).items():
            if neighbor not in visited:
                g_new = g + cost
                f_new = g_new + heuristics.get(neighbor,0)
                heapq.heappush(open_list,(f_new,g_new,neighbor,path + [neighbor]))
    return None,float("inf"),nodes_processed

def main():
    print("Enterprise Intelligent Routing Architecture")

    # Visual guide for the user so they know what keys are valid
    print("Available Network Hubs: S, A, B, C, D, E, F, G, H, I")
    print("(Try starting at 'S' and setting the destination to 'H')")

    start_node = input("\nIdentify Origin Hub: ").upper().strip()
    goal_node = input("Identify Destination Hub: ").upper().strip()

    if start_node not in network_map or goal_node not in network_map:
        print("Routing failed. Node target outside network infrastructure bounds.")
        return

    execution_matrix = []

    # Standard Breadth Exploration
    bfs_path,bfs_nodes = compute_bfs(network_map,start_node,goal_node)
    execution_matrix.append(("BFS", "->".join(bfs_path) if bfs_path else "Unreachable", "N/A", bfs_nodes))

    # Uniform Cost Optimisation
    ucs_path,ucs_cost,ucs_nodes = compute_ucs(network_map,start_node,goal_node)
    execution_matrix.append(("UCS", "->".join(ucs_path) if ucs_path else "Unreachable", ucs_cost, ucs_nodes))

    # Mathematical A* Optimization
    astar_path,astar_cost,astar_nodes = compute_astar(network_map,start_node,goal_node,target_heuristics)
    execution_matrix.append(("A*", "->".join(astar_path) if astar_path else "Unreachable", astar_cost, astar_nodes))

    print("\nBenchmark Analysis Matrix")
    print("Algorithm    | Path                 | Cost | Nodes Explored")
    for engine,route,expense,metrics in execution_matrix:
        print(f"{engine:<12} | {route:<20} | {expense:<4} | {metrics:<14}")

    if astar_path:
        print("\nOptimal Path Resolution Algorithm: A* Engine")
    else:
        print("\nTermination Status: Network path connection unavailable.")

if __name__ == "__main__":
    main()


# In[ ]:




