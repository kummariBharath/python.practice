def dfs(matrix, start_node):
    stack = [start_node]
    visited = []
    
    while stack:
        current = stack.pop()
        
        if current not in visited:
            visited.append(current)
            for neighbour in range(len(matrix[current])):
                if matrix[current][neighbour] == 1 and neighbour not in visited:
                    stack.append(neighbour)
                    
    return visited
