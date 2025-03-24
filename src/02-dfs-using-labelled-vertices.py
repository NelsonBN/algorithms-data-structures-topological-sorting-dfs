NOT_VISITED = 0
VISITING = 1
VISITED = 2

def topological_sort_dfs(graph):
    # Track the state of each vertex
    state = {}

    # Initialize states for all vertices
    for u in graph:
        state[u] = NOT_VISITED
        # Ensure all adjacent vertices are also included in our tracking dictionary
        for v in graph[u]:
            if v not in state:
                state[v] = NOT_VISITED

    # Result list to store the topological order
    result = []

    def dfs(vertex):
        # If the vertex is already processed, no need to visit again
        if state[vertex] == VISITED:
            return

        # If the vertex is currently being processed, we've detected a cycle
        if state[vertex] == VISITING:
            raise Exception("Graph contains at least one cycle - Topological sort is not possible")

        # Mark the vertex as being processed in the current traversal
        state[vertex] = VISITING

        # Process all adjacent vertices
        if vertex in graph: # Check if the vertex has any outgoing edges
            for adjacent in graph[vertex]:
                dfs(adjacent)

        # Mark the vertex as processed and no longer in the current traversal
        state[vertex] = VISITED

        result.append(vertex) # Push the vertex after visiting all neighbors (O(1))

    # Call DFS for each unvisited vertex
    for vertex in state:
        if state[vertex] == NOT_VISITED:
            dfs(vertex)

    # Reverse the list to get the correct topological order
    return result[::-1]


dag = {
    'A': ['B'],
    'B': ['C', 'D'],
    'C': ['E'],
    'D': ['E', 'F'],
    'E': ['G'],
    'F': ['G']
}

cycle = {
    'A': ['B'],
    'B': ['C'],
    'C': ['A'],
    'D': ['B', 'C'],
    'E': ['C', 'D']
}

graph = dag


print(f'Topological Sort: {topological_sort_dfs(graph)}')
