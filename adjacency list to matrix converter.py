def adjacency_list_matrix_converter(adj_list):
    num_nodes=len(adj_list)
    matrix=[[0 for _ in range(num_nodes)] for _ in range(num_nodes)]
    for node in adj_list:
        for neighbour in adj_list[node]:
            matrix[node][neighbour]=1
    return matrix  
A={
    0:[1,2],
    1:[2],
    2:[3,4],
    3:[4,5]
}
print(adjacency_list_matrix_converter(A))  #call the function

    