def adjacency_list_matrix_converter(adj_list):
    # Find the maximum node index in the dictionary to get the correct matrix size
    all_nodes = list(adj_list.keys()) # start with the keys of the dictionary, which are the nodes
    for neighbors in adj_list.values():# loop through the values of the dictionary, which are lists of neighbors
        all_nodes.extend(neighbors)
        
    num_nodes = max(all_nodes) + 1 if all_nodes else 0 # add 1 to get the correct size of the matrix, since node indices start at 0
    matrix=[[0 for _ in range(num_nodes)] for _ in range(num_nodes)]
    for node in adj_list:
        for neighbour in adj_list[node]:
            matrix[node][neighbour]=1
    for row in matrix:
        print(row)        
    return matrix  
A={
    0:[1,2],
    1:[2],
    2:[3,4],
    3:[4,5]
}
print(adjacency_list_matrix_converter(A))  #call the function

    